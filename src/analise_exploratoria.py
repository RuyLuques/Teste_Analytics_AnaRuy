import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/data_clean.csv")
df["Data"] = pd.to_datetime(df["Data"])

total_produto = df.groupby("Produto")["Total_Venda"].sum()

print("\nTotal de vendas por produto:")
print(total_produto)

produto_top = total_produto.idxmax()
print(f"\nProduto com maior venda total: {produto_top}")

df["Mes"] = df["Data"].dt.to_period("M")
vendas_mensais = df.groupby("Mes")["Total_Venda"].sum()

vendas_mensais.index = vendas_mensais.index.astype(str)

plt.figure()
vendas_mensais.plot()
plt.title("Tendência Mensal de Vendas - 2023")
plt.xlabel("Mês")
plt.ylabel("Total de Vendas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()