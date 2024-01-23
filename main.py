import math


def pearson_correlation(lst1, lst2):
    # r = (x - x_mean) * (y - y_mean) / math.sqrt((x - x_mean)**2 * (y - y_mean)**2)
    x_len = len(lst1)
    y_len = len(lst2)
    x_mean = sum(lst1)/x_len
    y_mean = sum(lst2)/y_len

    numerator = sum(map(lambda x, y: (x - x_mean) * (y - y_mean), lst1, lst2))

    denominator = math.sqrt(sum(map(lambda x: pow(x - x_mean, 2), lst1)))\
    * math.sqrt(sum(map(lambda y: pow(y - y_mean, 2), lst2)))

    if denominator == 0:
        return 0

    return numerator/denominator



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr1 = [3, 4, 5, 8, 9]
    arr2 = [9, 16, 25, 64, 81]

    print(pearson_correlation(arr1, arr2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
