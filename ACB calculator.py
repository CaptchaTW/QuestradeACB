import argparse
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument("file_name", type=str, nargs='?', help="QuestTrade File name")
args = parser.parse_args()
dictionary_acb = {}
dictionary_gains_loss = {}
file_name = args.file_name + ".csv"
df = pd.read_csv(file_name)
df1 = df[["Settlement Date","Action", "Symbol", "Quantity", "Net Amount", "Commission", "Currency"]]
df2 = df1.dropna()
#df2 = df2.reset_index(drop=True)

df_ca = df2[df2['Currency'].str.contains("CAD")].iloc[::-1]
df_usd = df2[df2['Currency'].str.contains("USD")].iloc[::-1]





def check_action(action, symbol, quantity, net_amount):
    if action == "Buy":
        add_acb(symbol,quantity,net_amount)
    elif action == "Sell":
        return
    else:
        return


def add_acb(symbol, quantity, net_amount):
    if symbol in dictionary_acb:
        return
    else:
        dictionary_acb[symbol] = (quantity, round(net_amount/quantity,3))


for index, row in df_ca.iterrows():
    check_action(row["Action"], row['Symbol'], row['Quantity'], row['Net Amount'])


print(dictionary_acb)