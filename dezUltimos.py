import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv ("manchas.csv")
x = data["Ano"]
y = data["manchas"]

data10st = data[167:177]
dataAno = data10st["Ano"]
dataPib = data10st["manchas"]

graph = plt.plot(dataAno, dataPib)
plt.show(graph)

