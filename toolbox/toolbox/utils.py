# General utility functions.
def normalize(signal):
    """Normalize a signal to range [0, 1]."""
    return (signal - min(signal)) / (max(signal) - min(signal))
