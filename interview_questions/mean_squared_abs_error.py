"""
Define mean squared error loss. In which cases is MSE used? How is it different
from mean absolute error?

Implement a Python function that computes MSE, and implement a separate
function for MAE.
"""
import numpy as np


def mse(y_true, y_pred):
    return np.mean(np.power(y_true - y_pred, 2))


def mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))
