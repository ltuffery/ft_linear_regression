import matplotlib.pyplot as plt
import pandas as pd

new = pd.read_csv('new.csv')
data = pd.read_csv('csv/data.csv')

plt.plot(new['km'], new['price'], 'r')
plt.plot(data['km'], data['price'], 'g')

plt.xlabel('Km')
plt.ylabel('Price')
plt.title('Graphique Linéaire de la Data')

plt.show()
