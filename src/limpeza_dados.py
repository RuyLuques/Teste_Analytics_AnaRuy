import pandas as pd

df = pd.read_csv("data/raw/data_simulated.csv")

df["Data"] = pd.to_datetime(df["Data"])

df["Preço"] = df["Preço"].fillna(df["Preço"].mean())
df["Produto"] = df["Produto"].fillna("Produto_Desconhecido")

df.drop_duplicates(inplace=True)

df["Total_Venda"] = df["Quantidade"] * df["Preço"]

df.to_csv("data/processed/data_clean.csv", index=False)

print("Limpeza concluída com sucesso.")