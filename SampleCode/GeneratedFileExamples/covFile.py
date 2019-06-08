import pandas as pd
from sklearn.linear_model import LinearRegression


# expand function for all type of file


def csvRead(file, Y=None):
    data = pd.read_csv(file)
    if(Y == None):
        return data
    else:
        y = data[Y]
        X = data.drop([Y], axis=1)
        return X, y


# linear regression model


def linearRegression(X, y, fit_intercept=True):
    model = LinearRegression(fit_intercept)
    model.fit(X, y)
    return model


# Predict Function
def predict(X, model):
    pred = model.predict(X)
    return pred


if __name__ == "__main__":
    X0, y0 = CSVRead(user, Y=label)
    model1 = Linear Regression(X0, y0, fit_intercept=True)
    pred2 = Prediction(user, model1)
