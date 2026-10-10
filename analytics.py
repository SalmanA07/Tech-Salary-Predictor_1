def calculate_average(salaries):
    """Calculates the average salary from a list."""
    size = len(salaries)
    if size == 0:
        return 0

    total_sum = sum(salaries)
    return total_sum / size


def find_max(salaries):
    """Finds the maximum salary in a list."""
    if len(salaries) == 0:
        return 0
    return max(salaries)


def find_min(salaries):
    """Finds the minimum salary in a list."""
    if len(salaries) == 0:
        return 0
    return min(salaries)


def train_salary_predictor(x, y):
    """Trains a simple linear regression model from scratch.

    Returns the slope (m) and intercept (b).
    """
    n = len(x)
    if n == 0:
        return 0, 0

    sum_x = sum(x)
    sum_y = sum(y)

    # Core linear regression formulas
    sum_xy = sum(x_val * y_val for x_val, y_val in zip(x, y))
    sum_xx = sum(x_val**2 for x_val in x)

    mean_x = sum_x / n
    mean_y = sum_y / n

    numerator = sum_xy - (n * mean_x * mean_y)
    denominator = sum_xx - (n * mean_x * mean_x)

    slope = numerator / denominator if denominator != 0 else 0
    intercept = mean_y - (slope * mean_x)

    return slope, intercept


def predict_salary(experience, slope, intercept):
    """Predicts a salary based on input years of experience."""
    return (slope * experience) + intercept