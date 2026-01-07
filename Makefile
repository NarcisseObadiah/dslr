.PHONY: help install setup clean run-describe run-histogram run-scatter run-pairplot train predict

# Default target
help:
	@echo "DSLR Project - Available Commands"
	@echo "=================================="
	@echo "make setup          - Create and activate virtual environment"
	@echo "make install        - Install project dependencies"
	@echo "make clean          - Remove virtual environment and cache files"
	@echo "make run-describe   - Run statistical analysis"
	@echo "make run-histogram  - Generate histogram visualization"
	@echo "make run-scatter    - Generate scatter plot visualization"
	@echo "make run-pairplot   - Generate pair plot visualization"
	@echo "make train          - Train logistic regression models"
	@echo "make predict        - Make predictions on test data"

# Setup virtual environment
setup:
	@echo "Setting up virtual environment..."
	python3 -m venv venv --without-pip
	@echo "Virtual environment created!"
	@echo "Activate it with: source venv/bin/activate (Linux/Mac)"

# Install dependencies
install: setup
	@echo "Installing dependencies..."
	bash -c 'source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
	@echo "Dependencies installed successfully!"

# Clean up
clean:
	@echo "Cleaning up..."
	rm -rf venv
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo "Cleanup complete!"

# Run analysis scripts
run-describe:
	@bash -c 'source venv/bin/activate && python src/describe.py datasets/dataset_train.csv'

run-histogram:
	@bash -c 'source venv/bin/activate && python src/histogram.py'
	@echo "Histogram saved to output/histogram.png"

run-scatter:
	@bash -c 'source venv/bin/activate && python src/scatter_plot.py'
	@echo "Scatter plot saved to output/scatter_plot.png"

run-pairplot:
	@bash -c 'source venv/bin/activate && python src/pair_plot.py'
	@echo "Pair plot saved to output/pair_plot.png"

# Training and prediction
train:
	@bash -c 'source venv/bin/activate && python src/logreg_train.py datasets/dataset_train.csv'

predict:
	@bash -c 'source venv/bin/activate && python src/logreg_predict.py datasets/dataset_test.csv'
	@echo "Predictions saved to output/houses.csv"

# Run all visualizations
visualize: run-describe run-histogram run-scatter run-pairplot
	@echo "All visualizations complete!"

# Full pipeline: setup, install, train, predict
all: install train predict visualize
	@echo "Full pipeline complete!"
