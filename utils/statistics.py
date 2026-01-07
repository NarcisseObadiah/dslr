# Custom Statistics Module
# Implements statistical functions (count, mean, std, percentiles)
# Handles NaN values (v == v checks for NaN)

import math

def count(values):
    """Count non-NaN values"""
    return len([v for v in values if v == v])

def mean(values):
    """Calculate mean of non-NaN values"""
    valid = [v for v in values if v == v]
    return sum(valid) / len(valid) if valid else float("nan")

def std(values):
    """Calculate standard deviation of non-NaN values"""
    valid = [v for v in values if v == v]
    if len(valid) < 2:
        return float("nan")
    avg = mean(valid)
    variance = sum((v - avg) ** 2 for v in valid) / (len(valid) - 1)
def min_value(values):
    """Find minimum of non-NaN values"""
    valid = [v for v in values if v == v]
    return min(valid) if valid else float("nan")

def max_value(values):
    """Find maximum of non-NaN values"""
    valid = [v for v in values if v == v]
    return max(valid) if valid else float("nan")

def percentile(values, percent):
    """Calculate percentile of non-NaN values"""lse float("nan")

def percentile(values, percent):
    valid = sorted([v for v in values if v == v])
    if not valid:
        return float("nan")
    index = int((percent / 100) * (len(valid) - 1))
    return valid[index]
