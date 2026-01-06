# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scatter_plot.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lhasmi <lhasmi@student.42heilbronn.de>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/06 22:07:10 by lhasmi            #+#    #+#              #
#    Updated: 2026/01/06 22:07:11 by lhasmi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/dataset_train.csv")

sns.scatterplot(
    data=df,
    x="Astronomy",
    y="Defense Against the Dark Arts",
    hue="Hogwarts House"
)

plt.savefig("output/scatter_plot.png")
