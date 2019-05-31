# imports
from sklearn.linear_model import LinearRegression
import numpy as np

# Model Function
"""
Linear Regression
Docs--
"""


def SimpleLinearRegression(fit_intercept=True, normalize=False):
    reg = LinearRegression(fit_intercept, normalize)
    return reg


# Train Function
"""
Sklearn module training function
Docs--
model accept previous function input
"""


def train(X, y, model):
    model.fit(X, y)
    return model


# Predict Function
"""
Sklearn module prediction function
Docs--
model accept previous function input
"""


def predict(X, model):
    return model.predict(X)


if __name__ == "__main__":
    a = SimpleLinearRegression(True, False)
    b = train([[0], [1], [2]], [[0], [1], [2]], a)
    c = predict([[0]], b)
