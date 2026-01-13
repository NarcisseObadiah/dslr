# Scatter plot analysis between two features
# Visualizes relationship between Astronomy and Defense Against the Dark Arts by House

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pathlib import Path

df = pd.read_csv("datasets/dataset_train.csv")

sns.scatterplot(
    data=df,
    x="Astronomy",
    y="Defense Against the Dark Arts",
    hue="Hogwarts House"
)

Path("output").mkdir(exist_ok=True)
plt.savefig("output/scatter_plot.png")
