import numpy as np
import simpleaudio as sa
import time

def beep(freq=1000, duration=0.5, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # gerar onda senoidal
    tone = np.sin(freq * 2 * np.pi * t)

    # normalizar para 16 bits
    audio = tone * (2**15 - 1)
    audio = audio.astype(np.int16)

    # tocar som
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    play_obj.wait_done()

# beep()
# time.sleep(1)
# beep(440, 0.5)   # som grave
# beep(880, 0.5)   # som mais agudo
# time.sleep(1)
# beep(1500, 0.3)  # beep curto

# beep(1000, 0.2)
beep(1200, 0.2)
# beep(1500, 0.2)