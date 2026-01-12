import numpy as np

LINE = "-" * 50

def print_array(arr, max_items=5):
    """Nicely print the first few values of a numpy array"""
    preview = ", ".join(f"{v: .4f}" for v in arr[:max_items])
    more = " ..." if len(arr) > max_items else ""
    print(f"[{preview}{more}]")

def show_model(path="models/model.npy"):
    model = np.load(path, allow_pickle=True).item()

    print("\n" + LINE)
    print(" LOGISTIC REGRESSION MODEL SUMMARY")
    print(LINE)

    print("\nSaved components:")
    for key in model.keys():
        print(f"  • {key}")

    print("\n" + LINE)
    print(" NORMALIZATION PARAMETERS")
    print(LINE)

    print("\nMean (first values):")
    print_array(model["mean"])

    print("\nStandard deviation (first values):")
    print_array(model["std"])

    print("\n" + LINE)
    print(" MODEL WEIGHTS (ONE-VS-ALL)")
    print(LINE)

    for house, weights in model["weights"].items():
        print(f"\nHouse: {house}")
        print(f"  Number of weights : {len(weights)}")
        print(f"  Bias term         : {weights[0]: .4f}")
        print("  Feature weights  :")
        print_array(weights[1:])

    print("\n" + LINE)
    print(" End of model summary")
    print(LINE + "\n")

if __name__ == "__main__":
    show_model()

