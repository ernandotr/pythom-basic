import numpy as np
import sounddevice as sd
import time

sample_rate = 44100

def play_note(freq, duration=0.3, volume=0.5):

    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    tone = np.sin(2 * np.pi * freq * t)

    # pequeno fade para evitar "click"
    fade = int(sample_rate * 0.01)
    envelope = np.ones_like(tone)
    envelope[:fade] = np.linspace(0, 1, fade)
    envelope[-fade:] = np.linspace(1, 0, fade)

    audio = volume * tone * envelope

    sd.play(audio, sample_rate)
    sd.wait()

# Exemplo de uso
NOTES = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88
}

melody = ["E","D","C","D","E","E","E"]

for note in melody:
    play_note(NOTES[note], 0.35)
time.sleep(0.5)
melody = [
    ("E",0.2),
    ("G",0.2),
    ("A",0.2),
    ("G",0.2),
    ("E",0.2),
    ("D",0.2),
    ("C",0.3),
]

for note, dur in melody:
    play_note(NOTES[note], dur)