import matplotlib.pyplot as plt
import pandas as pd
from predict_price import predict_price


def main():
    theta0, theta1 = 0.0, 0.0

    try:
        with open('./weight', 'r') as file:
            theta0, theta1 = map(float, file.read().split())
    except FileNotFoundError:
        pass

    data = pd.read_csv('csv/data.csv')
    prices = []

    for km in data['km']:
        prices.append(predict_price(km, theta0, theta1))

    plt.plot(data['km'], prices, 'r')
    plt.scatter(data['km'], data['price'])

    plt.xlabel('Km')
    plt.ylabel('Prix')
    plt.title('Graphique Linéaire de la Data')

    plt.show()


if __name__ == "__main__":
    main()