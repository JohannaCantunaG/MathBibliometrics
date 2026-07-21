import pandas as pd
from pathlib import Path

def parse_author_ids(author_str):
    
    if not isinstance(author_str, str) or not author_str.strip():
        return []
    ids = []
    for x in author_str.split(';'):
        x = x.strip()
        if x:
            try:
                ids.append(int(x))
            except ValueError:
                ids.append(x)
    return ids

def load_data_set(
        path_data,
        name_data,
        prefix = ""
    ):
    
    folder = path_data / name_data
    pattern = f"{prefix}{name_data}"
    csv_files = sorted(folder.glob(f"{pattern}_*.csv"))
    
    if not csv_files:
        raise FileNotFoundError(f"Don't find CSV files in {folder}")
    
    df_list = [pd.read_csv(f) for f in csv_files]
    df = pd.concat(df_list, ignore_index=True)

    df["ID_authors"] = df["Author(s) ID"].apply(parse_author_ids)
    df['Year'] = df['Year'].astype(int)
    df['n_authors'] = df['ID_authors'].apply(len)
    df = df.sort_values(by="Year", ascending=False).reset_index(drop=True)

    return df

def load_all_fields(
        path_data,
        fields,
        include_preperiod = False,
        add_field_column=True
    ):
    
    base = Path(path_data)

    dfs_by_field = {}
    df_all_list = []

    for field in fields:
        
        df_main = load_data_set(base, field, prefix="")
        
        if include_preperiod:
            try:
                df_pre = load_data_set(base, field, prefix="0_")
                df = pd.concat([df_pre, df_main], ignore_index=True)
            except FileNotFoundError:
                df = df_main
        else:
            df = df_main

        df = df.sort_values(by="Year", ascending = False).reset_index(drop=True)
        
        if add_field_column:
            df = df.copy()
            df["Field"] = field

        dfs_by_field[field] = df
        df_all_list.append(df)

    df_all = pd.concat(df_all_list, ignore_index=True)

    return dfs_by_field, df_all

def build_full_for_community(
        df_main, 
        df_hist
    ):

    df_full = pd.concat([df_hist, df_main], ignore_index=True)
    if "EID" in df_full.columns:
        df_full = df_full.drop_duplicates(subset=["EID"])

    df_full["Year"] = df_full["Year"].astype(int)
    return df_full