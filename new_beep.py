import numpy as np
import sounddevice as sd

def beep(freq=440, duration=0.5, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # gerar senoide
    tone = amplitude * np.sin(2 * np.pi * freq * t)

    # tocar som
    sd.play(tone, sample_rate)
    sd.wait()

# beep(440, 0.5)   # som grave
# beep(880, 0.5)   # som mais agudo
# beep(1500, 0.3)  # beep curto

# beep(1000, 0.2)
# beep(1200, 0.2)
# beep(1500, 0.2)

pattern = [
    (800, 0.2),
    (1000, 0.2),
    (1200, 0.2),
]

for freq, dur in pattern:
    beep(freq, dur)