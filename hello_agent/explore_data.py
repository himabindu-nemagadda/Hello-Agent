from pathlib import Path

import pandas as pd

data_folder = Path(__file__).parent / "data"
dataframes = {}

for csv_file in data_folder.glob("*.csv"):
    dataframe = pd.read_csv(csv_file)
    dataframes[csv_file.name] = dataframe

for filename, dataframe in dataframes.items():
    print(f"\nFilename: {filename}")
    print("First five rows:")
    print(dataframe.head())
    print("Column names:")
    print(dataframe.columns)
    print("Shape (rows, columns):")
    print(dataframe.shape)

print(dataframes["hospital_policy.csv"])
