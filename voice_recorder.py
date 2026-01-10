# pip install sounddevice scipy

import sounddevice as sd, scipy.io.wavfile as wav

sec = int(input("Enter the duration in seconds: "))
fs = 44100
print("Recording...")
recording = sd.rec(sec * fs, samplerate=fs, channels=2)
sd.wait()

wav.write("recording.wav", fs, recording)
print("Recording saved as 'recording.wav'")
