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
	rm -rf $(VENV) weights.npy output/

describe: venv
	$(PY) describe.py datasets/dataset_train.csv

train: venv
	$(PY) logreg/logreg_train.py datasets/dataset_train.csv

predict: venv
	$(PY) logreg/logreg_predict.py datasets/dataset_test.csv

histogram: venv
	$(PY) plots/histogram.py

scatter: venv
	$(PY) plots/scatter_plot.py

pairplot: venv
	$(PY) plots/pair_plot.py

plots: histogram scatter pairplot

all: install describe train predict plots

help:
	@echo "make install   - setup venv and dependencies"
	@echo "make describe  - show dataset statistics"
	@echo "make train     - train logistic regression model"
	@echo "make predict   - predict houses on test data"
	@echo "make plots     - generate all visualizations"
	@echo "make all       - run full pipeline"
	@echo "make clean     - remove venv and outputs"