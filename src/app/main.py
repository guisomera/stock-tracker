import pandas as pd

data = pd.read_csv("dados.csv", sep=",")
df = pd.DataFrame(data)
df["qtd_signed"] = df["qtd_bruta"]

df.loc[df["tipo"] == "Saida", "qtd_signed"] = df["qtd_bruta"] * -1
#Pandas, pegue todas as linhas onde o tipo é saida e na coluna qtd_signed, coloque o numero * -1

print(df)