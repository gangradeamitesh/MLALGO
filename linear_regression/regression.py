import numpy as np


class LinearRegression:

    def __init__(self) -> None:
        self.coefficients = None
        self.intercept = None

    def fit(self , X , y):
        X = np.array(X)
        y = np.array(y)

        X_b = np.c_[np.ones((X.shape[0] , 1)) , X]
        theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b,T).dot(y)

        self.intercept = theta_best[0]
        self.coefficients = theta_best[1:]

    def predict(self , X):
        X = np.array(X)
        X_b = np.c_[np.ones((X.shape[0],1)),X]
        return X_b.dot(np.r_[self.intercept , self.coefficients])
    
    def get_coefficients(self):
        return self.coefficients
    
    def get_intercept(self):
        return self.intercept