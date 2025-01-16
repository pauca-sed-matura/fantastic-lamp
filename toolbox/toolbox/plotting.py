# Module for plotting and visualization.
import matplotlib.pyplot as plt
import numpy as np

def plot_signal(signal, sampling_rate):
    """Plot a signal over time."""
    time = np.arange(len(signal)) / sampling_rate
    plt.plot(time, signal)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()
