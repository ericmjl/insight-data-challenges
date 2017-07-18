"""
Define mean squared error loss. In which cases is MSE used? How is it different
from mean absolute error?

Implement a Python function that computes MSE, and implement a separate
function for MAE.

Follow-on: In the case of linear regression, how do the loss functions change
when doing Ridge and Lasso regression?
"""
import numpy as np


def mse(y_true, y_pred):
    return np.mean(np.power(y_true - y_pred, 2))


def mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))
