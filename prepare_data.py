import pandas as pd
from pathlib import Path

data_path = Path("data") 

csv_files = list(data_path.glob("*.csv"))

frames = [pd.read_csv(f) for f in csv_files]
dataframe = pd.concat(frames, ignore_index=True)

dataframe = dataframe[dataframe["product"] == "pink morsel"].copy()
dataframe["price"] = dataframe["price"].str.replace("$", "").astype(float)
dataframe["sales"] = dataframe["quantity"] * dataframe["price"]
print (dataframe)

output = dataframe [["sales", "date", "region"]]
output.to_csv("data/pink_morsel_sales.csv", index=False)
