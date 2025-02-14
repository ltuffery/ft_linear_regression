def predict_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def main():
    theta0, theta1 = 0.0, 0.0

    try:
        with open('./weight.txt', 'r') as file:
            theta0, theta1 = map(float, file.read().split())
    except FileNotFoundError:
        pass

    mileage = float(input("Entrez le kilométrage de la voiture: "))

    price = predict_price(mileage, theta0, theta1)

    print(f"Le prix estimé pour un kilométrage de {mileage} est {price:.2f}.")


if __name__ == "__main__":
    main()