import numpy as np
import pandas as pd
from matplotlib import pyplot


def create_stat_matrix(m):
    matrix_x = np.zeros((215, m))
    with open('ratings.csv', 'r') as file:
        data = pd.read_csv(file)

    y = data.loc[data['movieId'].isin([1]), ['userId', 'rating']]
    matrix_y = y['rating'].values.reshape(-1, 1)
    x = data.loc[(data['movieId'] <= 10) & (data['userId'].isin(y['userId'])), ['userId', 'movieId', 'rating']].reset_index(drop=True)

    k = 0
    for i in range(len(matrix_x)):
        j = 0
        while j < m:
            if j+1 == x.loc[(x.index == k), ['movieId']].values:
                matrix_x[i][j] = x.loc[(x.index == k), ['rating']].values
                k += 1
            j += 1

    return matrix_x, matrix_y


def regression(matrix_x):
    num_of_elements = 0
    sum_of_products = 0
    sum_of_x = 0
    sum_of_x_pow = 0
    sum_of_y = 0
    x = []
    for i in range(1, len(matrix_x)+1):
        for j in range(len(matrix_x[i-1])):
            x.append(i)
            if matrix_x[i-1][j] != 0:
                num_of_elements += 1
                sum_of_products += i*matrix_x[i-1][j]
                sum_of_x += i
                sum_of_x_pow += i ** 2
                sum_of_y += matrix_x[i-1][j]

    avg_y = sum_of_y / num_of_elements
    avg_x = sum_of_x / num_of_elements
    slope = ((num_of_elements*sum_of_products) - (sum_of_x*sum_of_y))/((num_of_elements*sum_of_x_pow) - sum_of_x ** 2)
    intercept = avg_y - slope*avg_x

    x = np.array(x)
    y = [float('nan') if j == 0 else j for i in matrix_x for j in i]
    pyplot.scatter(x, y)
    pyplot.plot(x, intercept + x*slope, 'r')
    pyplot.show()

    return slope, intercept


def predict(matrix_x, matrix_y):
    slope, intercept = regression(matrix_x[:-15])
    predicted_ratings = []
    for i in range(199, 215):
        rating = intercept + slope*i
        predicted_ratings.append(rating)
    predicted_ratings = np.array(predicted_ratings)

    x = np.array([i for i in range(199, 215)])
    y = np.array([j for i in range(199, 215) for j in matrix_y[i]])
    pyplot.plot(x, predicted_ratings, 'r')
    pyplot.scatter(x, y)
    pyplot.show()


def learn(matrix):
    matrix_x, matrix_y = matrix
    predict(matrix_x, matrix_y)


learn(create_stat_matrix(10))
