import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv ("manchas.csv")
data.boxplot()
plt.show()
