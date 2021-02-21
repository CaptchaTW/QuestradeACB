import argparse
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument("file_name", type=str, nargs='?', help="QuestTrade File name")
args = parser.parse_args()

file_name = args.file_name + ".csv"
df = pd.read_csv(file_name)
df_useful = df[["Action", "Symbol", "Quantity", "Price", "Commission", "Currency"]]
print(df_useful)