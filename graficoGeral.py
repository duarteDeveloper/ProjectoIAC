import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv ("manchas.csv")
x = data["Ano"]
y = data["manchas"]
grafico = plt.plot(x, y)
plt.show(grafico)

