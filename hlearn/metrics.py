import numpy as np


def SMAPE(y_true, y_pred):
    losses = np.abs(y_true - y_pred) / (np.abs(y_true) + np.abs(y_pred)) * 2
    return np.mean(losses)
