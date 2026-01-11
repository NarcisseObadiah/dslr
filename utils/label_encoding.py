# Label Encoding Module
# Converts multi-class labels to one-vs-all binary classification format

def encode_one_vs_all(labels):
    houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    encoded = {}

    for house in houses:
        encoded[house] = (labels == house).astype(int)
    return encoded, houses