# DSLR - Data Science and Logistic Regression

A machine learning project for classifying Hogwarts Houses using student performance data.

## Project Structure

### `/src` - Main Analysis & ML Scripts
- **describe.py** - Statistical analysis of dataset (count, mean, std, percentiles, min/max)
- **histogram.py** - Visualize distribution of "Care of Magical Creatures" across houses
- **scatter_plot.py** - Scatter plot showing relationship between Astronomy and Defense Against the Dark Arts
- **pair_plot.py** - Multi-variable pairplot for selected features
- **logreg_train.py** - Train logistic regression models (one-vs-all for each house)
- **logreg_predict.py** - Make predictions on test data using trained models

### `/utils` - Helper Functions
- **data_cleaning.py** - Feature selection and missing value imputation
- **data_scaling.py** - Feature normalization (z-score)
- **label_encoding.py** - One-vs-all encoding for multi-class classification
- **statistics.py** - Custom statistical functions (count, mean, std, percentiles)

### `/datasets` - Data Files
- **dataset_train.csv** - Training data with student features and house labels
- **dataset_test.csv** - Test data for predictions

### `/models` - Trained Models
- **model.npy** - Saved weights from logistic regression training

### `/output` - Results
- **scatter_plot.png** - Scatter plot visualization
- **histogram.png** - Histogram visualization
- **pair_plot.png** - Pair plot visualization
- **houses.csv** - Prediction results on test data