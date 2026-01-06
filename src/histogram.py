# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    histogram.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lhasmi <lhasmi@student.42heilbronn.de>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/06 22:06:01 by lhasmi            #+#    #+#              #
#    Updated: 2026/01/06 22:06:02 by lhasmi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/dataset_train.csv")

sns.histplot(
    data=df,
    x="Care of Magical Creatures",
    hue="Hogwarts House",
    kde=True
)

plt.savefig("output/histogram.png")
