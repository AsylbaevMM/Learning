import math


def pearson_correlation(array_1: list, array_2: list):
    """

    :param array_1: первый массив значений
    :param array_2: второй массив значений
    :return: Корреляция Пирсона между массивами array_1 и array_2
    """

    # Проверка на то, что массивы одинаковой длины
    if len(array_1) != len(array_2):
        raise ValueError("Массивы должны быть одинаковой длины")

    n = len(array_1)

    # Расчет среднего значения
    mean_x = sum(array_1) / n
    mean_y = sum(array_2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in array_1])
    variance_y = sum([(yi - mean_y) ** 2 for yi in array_2])

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(array_1, array_2)])
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation


if __name__ == '__main__':
    arr_1 = [3, 5, 8, 15, 20, 25, 31, 35, 42]
    arr_2 = [2, 3, 4, 7, 12, 17, 23, 28, 33]

    print(f"Корреляция Пирсона: {round(pearson_correlation(arr_1, arr_2), 4)}")