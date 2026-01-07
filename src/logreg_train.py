# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_train.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lhasmi <lhasmi@student.42heilbronn.de>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/06 22:06:41 by lhasmi            #+#    #+#              #
#    Updated: 2026/01/06 22:06:42 by lhasmi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
import numpy as np
import pandas as pd

from utils.data_cleaning import prepare_features
from utils.data_scaling import normalize
from utils.label_encoding import encode_one_vs_all

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def train(features, labels, learning_rate=0.1, epochs=3000):
    samples, features_count = features.shape
    weights = np.zeros(features_count)

    for _ in range(epochs):
        prediction = sigmoid(features @ weights)
        gradient = (features.T @ (prediction - labels)) / samples
        weights -= learning_rate * gradient

    return weights

def main():
    if len(sys.argv) != 2:
        print("Usage: python logreg_train.py dataset_train.csv")
        return

    df = pd.read_csv(sys.argv[1])
    df = prepare_features(df, include_target=True)

    X = df.drop(columns=["Hogwarts House"]).values
    y = df["Hogwarts House"].values

    X, mean, std = normalize(X)
    X = np.hstack((np.ones((X.shape[0], 1)), X))

    encoded, houses = encode_one_vs_all(y)
    model_weights = {}

    for house in houses:
        model_weights[house] = train(X, encoded[house])

    np.save("models/model.npy", {
        "weights": model_weights,
        "mean": mean,
        "std": std
    })

    print("Training finished successfully.")

if __name__ == "__main__":
    main()
