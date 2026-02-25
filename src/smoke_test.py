import pandas as pd
import pathlib

data_path = pathlib.Path(__file__).parent.parent / "data" / "sample.csv"

df = pd.read_csv(data_path)

print("Shape:", df.shape)
print(df.head())
print(df.describe())