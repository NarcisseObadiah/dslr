# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_predict.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lhasmi <lhasmi@student.42heilbronn.de>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/06 22:06:33 by lhasmi            #+#    #+#              #
#    Updated: 2026/01/06 22:06:34 by lhasmi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
import numpy as np
import pandas as pd

from utils.data_cleaning import prepare_features
from utils.data_scaling import normalize

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def main():
    if len(sys.argv) != 2:
        print("Usage: python logreg_predict.py dataset_test.csv")
        return

    model = np.load("models/model.npy", allow_pickle=True).item()

    df = pd.read_csv(sys.argv[1])
    cleaned = prepare_features(df, include_target=False)

    X = cleaned.values
    X, _, _ = normalize(X, model["mean"], model["std"])
    X = np.hstack((np.ones((X.shape[0], 1)), X))

    probabilities = {}
    for house, weights in model["weights"].items():
        probabilities[house] = sigmoid(X @ weights)

    predictions = pd.DataFrame(probabilities).idxmax(axis=1)

    output = pd.DataFrame({
        "Index": df["Index"],
        "Hogwarts House": predictions
    })

    output.to_csv("output/houses.csv", index=False)
    print("Predictions saved.")

if __name__ == "__main__":
    main()
