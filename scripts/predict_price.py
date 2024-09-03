def predict_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def main():
    try:
        with open('../theta_values.txt', 'r') as file:
            theta0, theta1 = map(float, file.read().split())
    except FileNotFoundError:
        print("Veuillez d'abord entraîner le modèle pour générer theta_values.txt.")
        return

    mileage = float(input("Entrez le kilométrage de la voiture: "))

    price = predict_price(mileage, theta0, theta1)

    print(f"Le prix estimé pour un kilométrage de {mileage} est {price:.2f}.")


if __name__ == "__main__":
    main()
