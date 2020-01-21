import pandas as pd
import matplotlib.pyplot as plt
plt.title("RESULTADO DAS MANCHAS ENTRE O ANO 1753 AO ANO 1758 \n")
data = pd.read_csv ("manchas.csv")
years = data[4:10]
x = years["Ano"]
y = years["manchas"]
plt.subplots_adjust(bottom = 0.30)
plt.xlabel("ANO")
plt.ylabel("NÍVEL DE MANCHAS")
plt.grid(True)
plt.plot(x, y,'orange')
plt.xticks(x, x, rotation="vertical")
plt.show()

