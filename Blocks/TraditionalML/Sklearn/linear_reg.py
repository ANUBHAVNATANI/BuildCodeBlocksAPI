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
