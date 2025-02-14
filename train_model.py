import numpy as np

LEARNING_RATE = 0.01
ITERATIONS = 1500

def load_data(file_path):
    """
    Loads data from a CSV file.

    This function reads a CSV file containing mileage and price data.
    It returns two arrays: one for mileage and one for price.

    Parameters:
        file_path (str): The path to the CSV file to load.

    Returns:
        tuple: Two NumPy arrays, the first for mileage and the second for price.
    """
    data = np.loadtxt(file_path, delimiter=',', skiprows=1)
    mileage = data[:, 0]
    price = data[:, 1]
    return mileage, price


def normalize_data(data):
    """
    Normalizes the data by centering and scaling.

    This function applies the following transformation to the data:
    (data - mean) / std, where `mean` is the mean and `std` is the standard deviation of the data.

    Parameters:
        data (array-like): The data to normalize.

    Returns:
        tuple: A tuple containing:
            - The normalized data (array-like).
            - The mean of the original data (float).
            - The standard deviation of the original data (float).
    """
    mean = np.mean(data)
    std = np.std(data)
    normalized_data = (data - mean) / std
    return normalized_data, mean, std


def gradient_descent(mileage, price, theta0, theta1):
    """
    Performs gradient descent to adjust the model parameters.

    This function uses the gradient descent algorithm to minimize the cost by updating
    the parameters theta0 and theta1 in each iteration.

    Parameters:
        mileage (array-like): The mileage data.
        price (array-like): The price data.
        theta0 (float): The initial intercept term of the model.
        theta1 (float): The initial slope term of the model.

    Returns:
        tuple: A tuple containing the updated values of theta0 and theta1.
    """
    m = len(price)

    for _ in range(ITERATIONS):
        predictions = theta0 + theta1 * mileage
        tmp_theta0 = theta0 - LEARNING_RATE * (1 / m) * np.sum(predictions - price)
        tmp_theta1 = theta1 - LEARNING_RATE * (1 / m) * np.sum((predictions - price) * mileage)

        theta0, theta1 = tmp_theta0, tmp_theta1
    return theta0, theta1


def main():
    try:
        mileage, price = load_data('./csv/data.csv')
    except Exception:
        print("data.csv not found...")
        return

    normalized_mileage, mileage_mean, mileage_std = normalize_data(mileage)
    normalized_price, price_mean, price_std = normalize_data(price)

    theta0 = 0.0
    theta1 = 0.0

    theta0, theta1 = gradient_descent(normalized_mileage, normalized_price, theta0, theta1)

    theta1 = theta1 * price_std / mileage_std
    theta0 = price_mean - theta1 * mileage_mean

    with open('./weight', 'w') as file:
        file.write(f"{theta0} {theta1}")

    print(f"Modèle entraîné : theta0 = {theta0:.4f}, theta1 = {theta1:.4f}")


if __name__ == "__main__":
    main()