import argparse
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument("file_name", type=str, nargs='?', help="QuestTrade File name")
args = parser.parse_args()

file_name = args.file_name + ".csv"
df = pd.read_csv(file_name)
df1 = df[["Action", "Symbol", "Quantity", "Price", "Commission", "Currency"]]
df2 = df1.dropna()
#df2 = df2.reset_index(drop=True)

df_ca = df2[df2['Currency'].str.contains("CAD")]
df_usd = df2[df2['Currency'].str.contains("USD")]
print(df_ca)