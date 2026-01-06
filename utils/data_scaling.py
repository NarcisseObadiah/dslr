import numpy as np

def normalize(matrix, mean=None, std=None):
    if mean is None:
        mean = np.mean(matrix, axis=0)
    if std is None:
        std = np.std(matrix, axis=0)
        std[std == 0] = 1

    normalized = (matrix - mean) / std
    return normalized, mean, std
