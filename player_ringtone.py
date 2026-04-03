import numpy as np
import sounddevice as sd

sample_rate = 44100

# distância em semitons a partir de A4
NOTE_INDEX = {
    "C": -9, "C#": -8,
    "D": -7, "D#": -6,
    "E": -5,
    "F": -4, "F#": -3,
    "G": -2, "G#": -1,
    "A": 0,  "A#": 1,
    "B": 2
}

def note_to_freq(note):
    name = note[:-1]
    octave = int(note[-1])

    semitone = NOTE_INDEX[name] + (octave - 4) * 12
    return 440 * (2 ** (semitone / 12))


def play_note(freq, duration):

    t = np.linspace(0, duration, int(sample_rate * duration), False)
    # tone = np.sin(2 * np.pi * freq * t)
    tone = np.sign(np.sin(2 * np.pi * freq * t))

    # fade in/out
    fade_len = int(sample_rate * 0.01)
    envelope = np.ones_like(tone)

    envelope[:fade_len] = np.linspace(0, 1, fade_len)
    envelope[-fade_len:] = np.linspace(1, 0, fade_len)

    audio = 0.5 * tone * envelope

    sd.play(audio, sample_rate)
    sd.wait()


def play_song(song):

    for note, dur in song:
        if note == "REST":
            sd.sleep(int(dur * 1000))
        else:
            freq = note_to_freq(note)
            play_note(freq, dur)


# -------------------------------
# Exemplo: ringtone simples
# -------------------------------

nokia_style = [
    ("E5",0.18),
    ("D5",0.18),
    ("F#4",0.18),
    ("G#4",0.18),
    ("C#5",0.18),
    ("B4",0.18),
    ("D4",0.18),
    ("E4",0.18),
    ("B4",0.18),
    ("A4",0.18),
]

play_song(nokia_style)