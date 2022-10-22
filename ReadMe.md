## Audio Regeneration

Tried to regenerate song using Inverse short-time Fourier transform (ISFT) and Griffin-Lim Algorithm.

# Dependencies
- python 3.9
- librosa
- matlabplot

To setup environment run the following command:

`conda env create -f environment.yml`

activate environment :

`conda activate audio-regen-env`

To run

`python main.py`


# Spectrograms 

Original song (10 seconds duration)

![Original song](./spectrograms/Eminem.png)

Just 1 iteration

![Original song](./spectrograms/Regen%20Eminem%201.png)


500 iterations

![Original song](./spectrograms/Regen%20Eminem%20500.png)

500 iterations result is better in audio fidelity.