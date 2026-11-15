
# ==================================================
# Project: Grade Prediction Based on Socioeconomic Factors
# File: main.py
# Purpose: Main entry point of the project
# ==================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    """Run the main project program."""

    print("=" * 60)
    print("GRADE PREDICTION BASED ON SOCIOECONOMIC FACTORS")
    print("=" * 60)

    print("\nProject environment initialized successfully!")

    print("\nLibraries imported successfully:")
    print(f"Pandas version: {pd.__version__}")
    print(f"NumPy version: {np.__version__}")
    print(f"Matplotlib version: {plt.matplotlib.__version__}")
    print(f"Seaborn version: {sns.__version__}")


if __name__ == "__main__":
    main()
