# Multi-variable pairplot to visualize relationships between features
# Shows correlation patterns between Astronomy, Charms, Potions, and Flying

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pathlib import Path

df = pd.read_csv("datasets/dataset_train.csv")

selected = df[[
    "Astronomy",
    "Charms",
    "Potions",
    "Flying",
    "Hogwarts House"
]]

sns.pairplot(selected, hue="Hogwarts House", corner=True)
Path("output").mkdir(exist_ok=True)
plt.savefig("output/pair_plot.png")
