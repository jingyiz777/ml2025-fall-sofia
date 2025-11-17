import numpy
from sklearn.neighbors import KNeighborsRegressor

def main():

    # read N
    N = int(input("Enter number of points N: "))
    if N <= 0:
        print("N must be positive")
        return

    # read k
    k = int(input("Enter k: "))
    if k <= 0:
        print("k must be positive")
        return

    # make numpy arrays
    data_x = numpy.zeros((N, 1))
    data_y = numpy.zeros(N)

    # read points
    print("Enter the training points:")
    for i in range(N):
        x_val = float(input("x: "))
        y_val = float(input("y: "))
        data_x[i][0] = x_val
        data_y[i] = y_val

    # variance of y
    y_var = numpy.var(data_y, ddof=1)
    print("Variance of y:", y_var)

    # check k
    if k > N:
        print("Error: k cannot be larger than N")
        return

    # make model
    knn_model = KNeighborsRegressor(n_neighbors=k)
    knn_model.fit(data_x, data_y)

    # read X for prediction
    x_input = float(input("Enter X to predict Y: "))

    # predict Y
    y_output = knn_model.predict(numpy.array([[x_input]]))

    print("Predicted Y:", y_output[0])


if __name__ == "__main__":
    main()
