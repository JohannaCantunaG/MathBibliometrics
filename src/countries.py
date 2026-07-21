import re, unicodedata
import pandas as pd
import numpy as np

def _normalize_text(s):
    s = str(s)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower()
    s = re.sub(r"\s+", " ", s)
    return s.strip()

def _compile_patterns(country_patterns):
    return [(re.compile(pat), name) for pat, name in country_patterns.items()]

def _patterns_from_names(names):
    out = {}
    for name in names:
        norm = _normalize_text(name)
        norm_re = r"\b" + re.sub(r"\s+", r"\\s+", norm) + r"\b"
        out[norm_re] = name
    return out

def _dedup_preserve_order(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            out.append(x)
            seen.add(x)
    return out

def _normalize_set(strings):
    norm2canon = {}
    for x in strings:
        nx = _normalize_text(x)
        norm2canon[nx] = x
    return set(norm2canon.keys()), norm2canon

def find_missing_countries(
        df,
        col_affil,
        country_analise,
        world_countries,
        accepted_countries=None
    ):

    accepted_countries = set() if accepted_countries is None else set(accepted_countries)
    compiled = _compile_patterns(country_analise)
    world_norm_set, world_norm2canon = _normalize_set(world_countries)
    primary_names = set(country_analise.values())
    new_valid_hits = []
    noise_hits_aux = []
    countries = set()
    affil_series = df[col_affil] if col_affil in df.columns else pd.Series(dtype=object)

    for row_idx, affil_value in affil_series.items():
        if pd.isna(affil_value):
            continue

        text = _normalize_text(affil_value)
        parts = [p.strip() for p in text.split(';') if p.strip()]

        for chunk in parts:
            matched_primary = any(rx.search(chunk) for rx, _ in compiled)
            if matched_primary:
                continue

            tokens = [t.strip() for t in chunk.split(',') if t.strip()]
            if not tokens:
                continue

            last_norm = _normalize_text(tokens[-1])
            if last_norm in world_norm_set:
                canonical = world_norm2canon[last_norm]

                if canonical in primary_names or canonical in accepted_countries:
                    continue

                countries.add(canonical)
                new_valid_hits.append((row_idx, canonical, chunk))
            else:
                noise_hits_aux.append((row_idx, tokens[-1], chunk))

    hits = (pd.DataFrame(new_valid_hits, columns=["row","country","chunk"])
                           .sort_values(["country","row"], ignore_index=True))
    noise_hits = (pd.DataFrame(noise_hits_aux, columns=["row","token","chunk"])
                       .sort_values(["token","row"], ignore_index=True))

    return countries, hits, noise_hits

def tag_countries_from_affiliations(
        df,
        col_affil,
        country_patterns,
        out_col_list="countries_list",
        out_col_str="countries_str"
    ):
    
    compiled_patterns = _compile_patterns(country_patterns)
    results_list = []
    results_str  = []

    if col_affil not in df.columns:
        raise KeyError(f"Column '{col_affil}' was not found in the DataFrame")

    for affil_value in df[col_affil]:

        if pd.isna(affil_value):
            results_list.append(np.nan)
            results_str.append(np.nan)
            continue

        text = _normalize_text(affil_value)
        found = [country for regex, country in compiled_patterns if regex.search(text)]
        found = _dedup_preserve_order(found)
        results_list.append(found)
        results_str.append(";".join(found))

    df_out = df.copy()
    df_out[out_col_list] = results_list
    df_out[out_col_str]  = results_str
    return df_out