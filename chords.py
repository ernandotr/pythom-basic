import numpy as np
import sounddevice as sd

def chord(freqs, duration=0.5):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    tone = sum(np.sin(2 * np.pi * f * t) for f in freqs)
    tone = tone / len(freqs)

    sd.play(tone * 0.5, sample_rate)
    sd.wait()

# C major chord (C4, E4, G4)
chord([261.63, 329.63, 392.00], duration=1.0)


# chord([440, 550, 660], 1) 
