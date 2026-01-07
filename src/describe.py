# Statistical analysis tool for dataset exploration
# Calculates and displays statistical metrics for all numeric columns

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd
from utils.statistics import *

def main():
    if len(sys.argv) != 2:
        print("Usage: python describe.py dataset.csv")
        return

    df = pd.read_csv(sys.argv[1])
    numeric_df = df.select_dtypes(include=["float64", "int64"])

    for column in numeric_df.columns:
        values = numeric_df[column].tolist()
        print(f"\n{column}")
        print("Count:", count(values))
        print("Mean:", mean(values))
        print("Std:", std(values))
        print("Min:", min_value(values))
        print("25%:", percentile(values, 25))
        print("50%:", percentile(values, 50))
        print("75%:", percentile(values, 75))
        print("Max:", max_value(values))

if __name__ == "__main__":
    main()
