import unittest
from linear_regression.regression import LinearRegression


class TestLinearRegression(unittest.TestCase):

    def test_fit(self):
        X = [[1],[2],[3],[4]]
        y = [2,3,4,5]

        model = LinearRegression()
        model.fit(X , y)

        self.assertAlmostEqual(model.get_intercept() , 1)
        self.assertAlmostEqual(model.get_coefficients()[0] , 1)

    
    def test_predict(self):
        X = [[1],[2],[3],[4]]
        y = [2,3,4,5]

        model = LinearRegression()
        model.fit(X , y)

        predictions = model.predict([[5],[6]])
        self.assertAlmostEqual(predictions[0],6)
        self.assertAlmostEqual(predictions[1],7)

if __name__ == '__main__':
    unittest.main()