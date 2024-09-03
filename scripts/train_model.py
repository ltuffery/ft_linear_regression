import numpy as np


def load_data(file_path):
    data = np.loadtxt(file_path, delimiter=',', skiprows=1)
    mileage = data[:, 0]
    price = data[:, 1]
    return mileage, price


def normalize_data(data):
    mean = np.mean(data)
    std = np.std(data)
    normalized_data = (data - mean) / std
    return normalized_data, mean, std


def compute_cost(mileage, price, theta0, theta1):
    m = len(price)
    predictions = theta0 + theta1 * mileage
    cost = (1 / (2 * m)) * np.sum((predictions - price) ** 2)
    return cost


def gradient_descent(mileage, price, theta0, theta1, learning_rate, iterations):
    m = len(price)
    for _ in range(iterations):
        predictions = theta0 + theta1 * mileage
        tmp_theta0 = theta0 - learning_rate * (1 / m) * np.sum(predictions - price)
        tmp_theta1 = theta1 - learning_rate * (1 / m) * np.sum((predictions - price) * mileage)
        # Check for NaN or infinity values
        if np.isnan(tmp_theta0) or np.isnan(tmp_theta1) or np.isinf(tmp_theta0) or np.isinf(tmp_theta1):
            print("Warning: NaN or infinity values encountered during training. Consider reducing the learning rate.")
            break
        theta0, theta1 = tmp_theta0, tmp_theta1
    return theta0, theta1


def main():
    # Charger les données
    mileage, price = load_data('../csv/data.csv')

    # Normaliser les données
    normalized_mileage, mileage_mean, mileage_std = normalize_data(mileage)
    normalized_price, price_mean, price_std = normalize_data(price)

    # Initialiser les paramètres
    theta0 = 0.0
    theta1 = 0.0
    learning_rate = 0.01  # Reduce the learning rate
    iterations = 1500

    theta0, theta1 = gradient_descent(normalized_mileage, normalized_price, theta0, theta1, learning_rate, iterations)

    # Ajuster les paramètres pour la normalisation
    theta1 = theta1 * price_std / mileage_std
    theta0 = price_mean - theta1 * mileage_mean

    # Sauvegarder les valeurs de theta0 et theta1
    with open('../theta_values.txt', 'w') as file:
        file.write(f"{theta0} {theta1}")

    print(f"Modèle entraîné : theta0 = {theta0:.4f}, theta1 = {theta1:.4f}")


if __name__ == "__main__":
    main()
