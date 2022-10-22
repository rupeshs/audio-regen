import numpy as np
import matplotlib.pyplot as plt

import librosa
import librosa.display


def save_spectrogram(
    audio_path,
    song_name,
    save_path,
):
    y, sr = librosa.load(audio_path)
    D = librosa.stft(y)  # STFT of y
    S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
    fig, ax = plt.subplots()
    img = librosa.display.specshow(
        S_db, x_axis="time", y_axis="linear", ax=ax, cmap="viridis"
    )
    ax.set(title=song_name)
    fig.colorbar(img, ax=ax, format="%+2.f dB")

    plt.savefig(f"{save_path}/{song_name}.png")
    # plt.show()
