import pandas as pd
import numpy as np

n = 60

produtos = {
    "Notebook": "Eletrônicos",
    "Smartphone": "Eletrônicos",
    "Cadeira": "Móveis",
    "Mesa": "Móveis",
    "Fone de Ouvido": "Acessórios"
}

np.random.seed(42)

datas = pd.date_range(start="2023-01-01", end="2023-12-31", periods=n)

data = {
    "ID": range(1, n+1),
    "Data": datas,
    "Produto": np.random.choice(list(produtos.keys()), n),
    "Quantidade": np.random.randint(1, 10, n),
    "Preço": np.random.uniform(50, 5000, n).round(2)
}

df = pd.DataFrame(data)

df["Categoria"] = df["Produto"].map(produtos)

df.loc[5, "Preço"] = np.nan
df.loc[10, "Produto"] = np.nan

df = pd.concat([df, df.iloc[[0]]])

df.to_csv("data/raw/data_simulated.csv", index=False)

print("Dataset simulado criado com sucesso.")