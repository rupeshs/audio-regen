from audio_ops import read_audio_spectrum, generate_audio_signal, save_audio
from spectrograms import save_spectrogram

INPUT_FILE = r"./inputs/inputs_eminem.mp3"
RESULT_FILE = r"./results/inputs_eminem_regen_1.wav"

S, fs, p = read_audio_spectrum(INPUT_FILE)

save_spectrogram(
    INPUT_FILE,
    "Eminem",
    r"./spectrograms",
)

audio = generate_audio_signal(
    S,
    2048,
    1,
)
save_audio(
    RESULT_FILE,
    audio,
    fs,
)
save_spectrogram(
    RESULT_FILE,
    "Regen Eminem 1",
    r"./spectrograms",
)
