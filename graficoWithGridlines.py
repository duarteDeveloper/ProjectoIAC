import pandas as pd
import matplotlib.pyplot as plt
plt.title("RESULTADO DAS MANCHAS REGISTRADAS NOS PRIMEIROS 30 ANOS\n")
data = pd.read_csv ("manchas.csv")
years = data[0:20]
x = years["Ano"]
y = years["manchas"]
plt.subplots_adjust(bottom = 0.30)
plt.xlabel("ANO")
plt.ylabel("MANCHAS")
plt.grid(True)
plt.plot(x, y)
plt.xticks(x, x, rotation="vertical")
plt.show()

