"""
Config file for file names and directories for uniform file access across different notebooks.
"""

import os


# directories
DATA_DIR = os.path.join("..", "data")
OUTPUT_DIR = os.path.join("..", "output")
INTERMEDIATE_DIR = os.path.join("..", "intermediate")


# LOOV file names
LOOV_RES_NAME = "loov_res.csv"
LOOV_INPUT_NAME = "loov_input_data.csv"
MODEL_FILE_NAME = "best_model.skops"