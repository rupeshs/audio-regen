import librosa
import numpy as np
import soundfile as sf


def read_audio_spectrum(
    filename,
    n_fft_in=2048,
):
    audio, fs = librosa.load(filename)
    print(f"Audio time series shape : {audio.shape}")
    print(f"Sampling rate : {fs} Hz")
    # Converting audio signal to frequency domain
    S = librosa.stft(audio, n_fft=n_fft_in)
    phase = np.angle(S)
    S = np.log1p(np.abs(S))
    return S, fs, phase


def generate_audio_signal(
    S,
    n_fft_in=2048,
    iterations =100,
):
    a = np.zeros_like(S)
    a = np.expm1(S) #inverse of log(1 + x)
    p = 2 * np.pi * np.random.random_sample(a.shape) - np.pi
    for i in range(iterations):
        S = a * np.exp(1j * p)
        x = librosa.istft(S)
        p = np.angle(librosa.stft(x, n_fft=n_fft_in))

    return x


def save_audio(path, audio, fs):
    sf.write(
        path,
        audio,
        fs,
    )
