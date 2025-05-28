import pyttsx3

def speak(engine, text):
    engine.say(text)
    engine.runAndWait()

def change_voice(engine, language, gender='VoiceGenderNeuter'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))

if __name__ == "__main__":

    engine = pyttsx3.init()
    # for voice in engine.getProperty('voices'):
    #     print(voice)

    lenguage = 'pt_BR'  # Portuguese (Brazil
    lenguage2 = 'en_US'  # English (United States)
    lenguage3 = "fr_FR"  # French (France)
    # change_voice(engine, "nl_BE", "VoiceGenderFemale")
    # engine.say("Hello World")
    # engine.runAndWait()

    
    #Set the language French (France) and the first voice available
    # change_voice(engine, lenguage3, "VoiceGenderNeuter")  # Change to French (France) neuter voice
    engine.setProperty('voice', "com.apple.voice.compact.fr-FR.Thomas")  # Set to 
    speak(engine, "Bonjour, ceci est un test de conversion de texte en parole.")
    speak(engine, "Comment puis-je vous aider aujourd'hui ?")
    speak(engine, "Au revoir !")
    speak(engine, "Ceci est un exemple simple de conversion de texte en parole avec Python.")
    speak(engine, "Merci d'avoir utilisé ce programme.")
    speak(engine, "Passez une excellente journée !")
    speak(engine, "Ceci est une démonstration de la bibliothèque pyttsx3.")
    speak(engine, "N'hésitez pas à modifier le texte selon vos besoins.")
    speak(engine, "Ce code est conçu pour convertir du texte en parole.")
    speak(engine, "Vous pouvez l'utiliser pour diverses applications.")
    
