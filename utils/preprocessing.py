# Data preprocessing utilities
#data cleaning, scaling, and label encoding combined

import numpy as np

FEATURE_COLUMNS = [
    "Astronomy",
    "Muggle Studies",
    "Ancient Runes",
    "Charms",
    "Divination",
    "Potions",
    "Flying"
]

HOUSES = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

def prepare_features(dataframe, include_target=True):
    """
    Select numeric features and fill missing values with column mean.
    """
    columns = FEATURE_COLUMNS.copy()
    if include_target:
        columns.append("Hogwarts House")
    cleaned = dataframe[columns].copy()

    for col in FEATURE_COLUMNS:
        cleaned[col] = cleaned[col].fillna(cleaned[col].mean())
    return cleaned


def normalize(matrix, mean=None, std=None):
    """
    Z-score normalization (standardization)
    Pass mean/std from training to apply same scaling to test data
    """
    if mean is None:
        mean = np.mean(matrix, axis=0)
    if std is None:
        std = np.std(matrix, axis=0)
        std[std == 0] = 1

    normalized = (matrix - mean) / std
    return normalized, mean, std


def encode_one_vs_all(labels):
    """
    Convert house labels to one-vs-all binary format
    Returns dict with binary arrays for each house
    """
    encoded = {}
    for house in HOUSES:
        encoded[house] = (labels == house).astype(int)
    return encoded, HOUSES
