# DSLR Project Makefile
# Usage: make install && make train && make predict

PYTHON ?= /usr/bin/python3
VENV   := .venv
PY     := $(VENV)/bin/python

.PHONY: venv install clean describe train predict histogram scatter pairplot plots all help

# Setup
venv:
	@test -d $(VENV) || $(PYTHON) -m venv $(VENV)

install: venv
	$(PY) -m pip install -q --upgrade pip
	$(PY) -m pip install -q -r requirements.txt

clean:
	rm -rf $(VENV) models/*.npy output/*.png output/*.csv

# Analysis
describe: venv
	$(PY) src/describe.py datasets/dataset_train.csv

# ML Pipeline
train: venv
	$(PY) src/logreg_train.py datasets/dataset_train.csv

predict: venv
	$(PY) src/logreg_predict.py datasets/dataset_test.csv

# Visualizations
histogram: venv
	$(PY) src/histogram.py

scatter: venv
	$(PY) src/scatter_plot.py

pairplot: venv
	$(PY) src/pair_plot.py

plots: histogram scatter pairplot

# Run everything
all: install describe train predict plots

help:
	@echo "make install   - setup venv and dependencies"
	@echo "make describe  - show dataset statistics"
	@echo "make train     - train logistic regression model"
	@echo "make predict   - predict houses on test data"
	@echo "make plots     - generate all visualizations"
	@echo "make all       - run full pipeline"
	@echo "make clean     - remove venv and outputs"
