import pandas as pd
import numpy as np
from collections import Counter
from scipy.optimize import curve_fit

def publications_per_year(
        df, 
        name_column,
    ):
    
    pubs_per_year = df.groupby('Year').size().reset_index(name=name_column)
    
    return pubs_per_year

def document_type_share_by_year(
        df, 
        doc_types=("Conference paper", "Article")
    ):
    
    total = df.groupby("Year").size().rename("Total")
    counts = (df.groupby(["Year", "Document Type"]).size().unstack(fill_value=0))

    for dt in doc_types:
        if dt not in counts.columns:
            counts[dt] = 0

    result = pd.DataFrame(index=total.index)
    result["Total"] = total

    for dt in doc_types:
        result[f"{dt}_count"] = counts[dt]
        result[f"{dt}_percent"] = (counts[dt] / total * 100)

    result = result.reset_index()

    return result

def compute_author_communities(
        df, 
        window=5
    ):

    df = df.copy()
    df['Year'] = df['Year'].astype(int)

    rows = []
    for _, row in df[['Year', 'ID_authors']].iterrows():
        year = row['Year']
        for aid in row['ID_authors']:
            rows.append((aid, year))
    auth_year = pd.DataFrame(rows, columns=['author_id', 'Year'])

    min_year = auth_year['Year'].min()
    max_year = auth_year['Year'].max()
    years = np.arange(min_year, max_year + 1)

    life = (auth_year.groupby('author_id')['Year']
            .agg(['min', 'max'])
            .rename(columns={'min': 'first', 'max': 'last'}))

    data = []

    for y in years:
        start = max(y - window + 1, min_year)
        mask_window = (auth_year['Year'] >= start) & (auth_year['Year'] <= y)
        sub = auth_year[mask_window]
        counts = sub['author_id'].value_counts()
        n_authors_5y = counts.index.nunique()
        n_authors_5y_gt1 = (counts >= 2).sum()
        mask_c = (life['first'] <= y) & (life['last'] >= y)
        n_comm_c = mask_c.sum()

        data.append({
            'Year': y,
            'Authors_5y': n_authors_5y,
            'Authors_5y_gt1pub': n_authors_5y_gt1,
            'Community_c': n_comm_c
        })

    return pd.DataFrame(data)

def compute_author_productivity(df):
    
    all_authors = [a for lst in df['ID_authors'] for a in lst]
    author_counts = Counter(all_authors)
    prod_df = pd.DataFrame.from_dict(author_counts, orient='index', columns=['n_pubs'])
    prod_df.index.name = 'author_id'
    prod_df.reset_index(inplace=True)
    freq = prod_df['n_pubs'].value_counts().sort_index()
    mean_prod = prod_df['n_pubs'].mean()

    return prod_df, freq, mean_prod

def clean_journal_counts(df):

    df_clean = df.dropna(subset=['Source title']).copy()
    journal_counts = (
    df_clean.groupby('Source title')
    .size()
    .sort_values(ascending=False))
    
    return journal_counts

def leimkuhler(x, a, b):
    return a * np.log(1 + b*x)

def bradford_stats(
        journal_counts, 
        top_frac=0.10,
    ):
    
    counts = journal_counts.sort_values(ascending=False).values
    ranks = np.arange(1, len(counts) + 1)
    cumulative = np.cumsum(counts)
    params, _ = curve_fit(leimkuhler, ranks, cumulative, maxfev=10000)
    a_fit, b_fit = params
    top_n = max(1, int(top_frac * len(counts)))
    publications_top = cumulative[top_n - 1]
    total = cumulative[-1]
    percent = publications_top / total * 100

    return {
        "ranks": ranks,
        "cumulative": cumulative,
        "a": a_fit,
        "b": b_fit,
        "top_n": top_n,
        "percent_top": percent,
        "n_journals": int(len(counts)),
        "total_pubs": float(total),
    }

def get_growth_segments(
        df,
        field,
        break_year,
        forced_models_growth,
        field_special=None,
        periods_special=None,
        labels_special = None,
    ):
    
    year_min = int(df["Year"].min())
    year_max = int(df["Year"].max())
    field_config = forced_models_growth.get(field, {})

    if field == field_special:
        periods = periods_special
        labels = labels_special
        models_by_segment = field_config.get("segments", [None] * len(periods))
        text_locations = ["tl", "tr", "bl"]
    else:
        periods = [(year_min, break_year), (break_year + 1, year_max)]
        labels = [f"PRE (≤{break_year})", f"POST (>{break_year})"]
        models_by_segment = [field_config.get("pre"), field_config.get("post")]
        text_locations = ["tl", "tr"]

    segments = []
    for period, label, models, text_location in zip(periods, labels, models_by_segment, text_locations):
        segments.append({
            "year_min": period[0],
            "year_max": period[1],
            "label": label,
            "models": models,
            "text_location": text_location,
        })

    return segments