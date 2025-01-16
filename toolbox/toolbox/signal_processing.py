# Module for DSP functions.
import numpy as np

def apply_fft(signal, sampling_rate):
    """Apply FFT to a signal."""
    freq = np.fft.fftfreq(len(signal), d=1/sampling_rate)
    fft_values = np.fft.fft(signal)
    return freq, np.abs(fft_values)
