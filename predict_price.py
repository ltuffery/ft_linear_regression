def predict_price(mileage, theta0, theta1):
    """
    Predicts the price based on the mileage using the linear regression model.

    This function uses the linear regression equation: 
    price = theta0 + theta1 * mileage to predict the price.

    Parameters:
        mileage (float): The mileage of the car.
        theta0 (float): The intercept term of the model.
        theta1 (float): The slope term of the model.

    Returns:
        float: The predicted price based on the given mileage.
    """
    return theta0 + theta1 * mileage


def main():
    theta0, theta1 = 0.0, 0.0

    try:
        with open('./weight', 'r') as file:
            theta0, theta1 = map(float, file.read().split())
    except FileNotFoundError:
        pass

    try:
        mileage = float(input("Entrez le kilométrage de la voiture: "))
    except Exception:
        print("\nValeur invalide")
        return

    price = predict_price(mileage, theta0, theta1)

    print(f"Le prix estimé pour un kilométrage de {mileage} est {price:.2f}.")


if __name__ == "__main__":
    main()