# Simple k-NN Regression using a class and numpy

import numpy as np

# We make a class to handle all the data and calculations
class KNNRegression:
    def __init__(self):
        # When we create this object, it starts with empty x and y lists
        self.x_values = []
        self.y_values = []

    # This function adds one (x, y) pair to our data
    def add_point(self, x, y):
        self.x_values.append(x)
        self.y_values.append(y)

    # This function does the actual k-NN regression
    def predict(self, X_input, k):
        # Convert the lists into numpy arrays (so we can use math easily)
        x_array = np.array(self.x_values)
        y_array = np.array(self.y_values)

        N = len(x_array)  # how many points we have

        # If k is bigger than how many points we have, it’s not valid
        if k > N:
            print("Error: k cannot be larger than N.")
            return None

        # Find how far each x point is from the X_input
        distances = np.abs(x_array - X_input)

        # Sort distances and pick the k smallest ones
        nearest_indices = np.argsort(distances)[:k]

        # Get the y values of those nearest neighbors
        nearest_y = y_array[nearest_indices]

        # Compute the mean (average) Y value
        Y_pred = np.mean(nearest_y)

        return Y_pred


# ---- Main program starts here ----
print("Welcome to k-NN Regression Program!")

# 1. Create an object from our class
model = KNNRegression()

# 2. Ask how many points we will enter
N = int(input("How many points (N)? "))

# 3. Ask for k (number of neighbors)
k = int(input("Enter k (number of neighbors): "))

# 4. Ask for each (x, y) point
for i in range(N):
    print("Point", i + 1)
    x = float(input("  Enter x value: "))
    y = float(input("  Enter y value: "))
    model.add_point(x, y)

# 5. Ask for X to predict
X_input = float(input("Enter X to predict Y: "))

# 6. Call the predict function
Y_pred = model.predict(X_input, k)

# 7. Show the result
if Y_pred is not None:
    print("Predicted Y =", Y_pred)