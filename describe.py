import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd
from utils.statistics import count, mean, std, min_value, max_value, percentile


def compute_stats(values):
    """Compute all statistics for a list of values."""
    return [
        count(values),
        mean(values),
        std(values),
        min_value(values),
        percentile(values, 25),
        percentile(values, 50),
        percentile(values, 75),
        max_value(values),
    ]

def format_table(columns, data, labels):
    width = {c: max(len(c), 15) for c in columns}
    label_w = 8
    
    print(" " * label_w + "".join(f"{c:>{width[c]}}  " for c in columns))
    print("-" * (label_w + sum(width[c] + 2 for c in columns)))
    
    for i, label in enumerate(labels):
        values = "".join(f"{data[c][i]:>{width[c]}.4f}  " for c in columns)
        print(f"{label:<{label_w}}{values}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python describe.py <dataset_file>")
        return
    try:
        df = pd.read_csv(sys.argv[1])
    except Exception as e:
        print(f"Error reading dataset: {e}")
        return

    numeric = df.select_dtypes(include=["float64", "int64"])
    columns = list(numeric.columns)
    
    stats_data = {col: compute_stats(numeric[col].tolist()) for col in columns}
    labels = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]
    
    format_table(columns, stats_data, labels)

if __name__ == "__main__":
    main()

