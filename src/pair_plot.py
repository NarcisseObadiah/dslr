# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pair_plot.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lhasmi <lhasmi@student.42heilbronn.de>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/06 22:06:51 by lhasmi            #+#    #+#              #
#    Updated: 2026/01/06 22:06:52 by lhasmi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/dataset_train.csv")

selected = df[[
    "Astronomy",
    "Charms",
    "Potions",
    "Flying",
    "Hogwarts House"
]]

sns.pairplot(selected, hue="Hogwarts House", corner=True)
plt.savefig("output/pair_plot.png")
