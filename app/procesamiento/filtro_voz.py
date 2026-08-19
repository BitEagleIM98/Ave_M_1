from scipy.signal import butter, lfilter


def bandpass_filter(data, fs, low=300, high=3400, order=6):
    nyq = 0.5 * fs
    low /= nyq
    high /= nyq
    b, a = butter(order, [low, high], btype='band')
    return lfilter(b, a, data)