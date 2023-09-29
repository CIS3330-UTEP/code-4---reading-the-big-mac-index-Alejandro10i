import pandas as pd

df = pd.read_csv("big-mac-full-index.csv")

query = f"(iso_a3=='NX' or iso_a3=='DNK' )"

df_result = df.query(query)

mean_dollar_price = df_result ['dollar_price'].mean()
