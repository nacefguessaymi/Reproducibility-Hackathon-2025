import polars as pl
def data_import():
    df = pl.read_parquet('hf://datasets/browndw/human-ai-parallel-corpus/**/*.parquet')
    data_path = "./data/"
    df.write_parquet(data_path + "data.parquet")
    return

data_import()