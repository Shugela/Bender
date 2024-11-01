# Makefile for Python project with venv and requirements

# Set up virtual environment
VENV_NAME := .venv
PYTHON := $(VENV_NAME)/bin/python3
PIP := $(VENV_NAME)/bin/pip3

# Set up dependencies
REQUIREMENTS := requirements.txt

# Default target
.PHONY: all
all: $(VENV_NAME) install

# Create virtual environment
$(VENV_NAME):
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV_NAME)

# Install dependencies
.PHONY: install
install:
	@echo "Installing dependencies..."
	pip install -r $(REQUIREMENTS)

# Run your program
.PHONY: run
run:
	@echo "Running your program..."
	$(PYTHON) your_program.py

# Clean up
.PHONY: clean
clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_NAME)

# Help target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  all        : Set up virtual environment and install dependencies"
	@echo "  install    : Install dependencies"
	@echo "  run        : Run your program"
	@echo "  clean      : Clean up virtual environment"
	@echo "  help       : Display this help message"
