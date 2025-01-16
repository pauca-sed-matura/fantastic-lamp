# Module for importing and cleaning ASCII data.
import pandas as pd

def load_ascii(file_path, delimiter=",", encoding="utf-8"):
    """Load ASCII data into a pandas DataFrame."""
    return pd.read_csv(file_path, delimiter=delimiter, encoding=encoding)
