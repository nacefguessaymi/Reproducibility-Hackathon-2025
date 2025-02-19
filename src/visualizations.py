import polars as pl

def open_data(input):
    df = pl.read_parquet(input)
    return df

def text_length(df):
    df