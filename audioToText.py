import speech_recognition as sr

recognizer = sr.Recognizer()

audio_file = "audio.wav"

from pydub import AudioSegment
AudioSegment.from_file(audio_file).export("audio.wav", format="wav")

with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        print("Transcription: ", text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# The above code converts an audio file from mp3 to wav format and then transcribes the wav file using Google Speech Recognition.
