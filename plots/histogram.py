# Histogram visualization for feature analysis
# Shows distribution of "Care of Magical Creatures" across Hogwarts Houses

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pathlib import Path

df = pd.read_csv("datasets/dataset_train.csv")

sns.histplot(
    data=df,
    x="Care of Magical Creatures",
    hue="Hogwarts House",
    kde=True
)

Path("output").mkdir(exist_ok=True)
plt.savefig("output/histogram.png")
