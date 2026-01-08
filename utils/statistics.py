# Custom Statistics Module
# Implements statistical functions (count, mean, std, percentiles)
# Handles NaN values (v == v checks for NaN)

import math

def count(values):

    valid_values = []

    for value in values:
        if value == value:  # Check for NaN
            valid_values.append(value)
    return len(valid_values)


def mean(values):
    valid_values = []
    for value in values:
        if value == value:  # Check for NaN
            valid_values.append(value)
    if len(valid_values) == 0:
        return float("nan")
    total_sum = 0
    for value in valid_values:
        total_sum += value
    return total_sum / len(valid_values)



def std(values):
    """Calculate standard deviation of non-NaN values"""
    valid_values = []
    for value in values:
        if value == value:
            valid_values.append(value)
    if len (valid_values) < 2:
        return float("nan")

    average = mean(valid_values)
    
    squared_differences = 0
    for value in valid_values:
        squared_differences += (value - average) ** 2
    variance = squared_differences / (len(valid_values) - 1)
    return math.sqrt(variance)

def min_value(values):
    valid_values = []
    for value in values:
        if value == value:
            valid_values.append(value)
    if len(valid_values) == 0:
        return float("nan")
    
    current_min = valid_values[0]
    for value in valid_values:
        if value < current_min:
            current_min = value
    return current_min



def max_value(values):
    valid_values = []
    for value in values:
        if value == value:
            valid_values.append(value)
    if len(valid_values) == 0:
        return float("nan")
    
    current_max = valid_values[0]
    for value in valid_values:
        if value > current_max:
            current_max = value
    return current_max

def percentile(values, percent):
    """Calculate percentile of non-NaN values"""
    valid_values = []

    for value in values:
        if value == value:
            valid_values.append(value)
    if len(valid_values) == 0:
        return float("nan")
    
    valid_values.sort()
    position = int((percent / 100) * (len(valid_values) - 1))
    return valid_values[position]
