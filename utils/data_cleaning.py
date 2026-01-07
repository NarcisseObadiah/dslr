# Data Cleaning Module
# Handles feature selection and missing value imputation

def prepare_features(dataframe, include_target=True):
    """
    Prepare dataset by selecting numeric features and handling missing values.
    Fills NaN values with column mean.
    """
    numeric_columns = [
        "Astronomy",
        "Muggle Studies",
        "Ancient Runes",
        "Charms",
        "Divination",
        "Potions",
        "Flying"
    ]

    columns = numeric_columns.copy()
    if include_target:
        columns.append("Hogwarts House")

    cleaned = dataframe[columns].copy()

    for column in numeric_columns:
        average = cleaned[column].mean()
        cleaned[column] = cleaned[column].fillna(average)

    return cleaned
