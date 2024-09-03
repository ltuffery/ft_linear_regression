import matplotlib.pyplot as plt
import pandas as pd

# Lire le fichier CSV
new = pd.read_csv('new.csv')
data = pd.read_csv('csv/data.csv')

# Tracer les données
plt.plot(new['km'], new['price'], 'r')
plt.plot(data['km'], data['price'], 'g')

# Ajouter des labels et un titre
plt.xlabel('Km')
plt.ylabel('Price')
plt.title('Graphique Linéaire de la Data')

# Afficher le graphique
plt.show()
