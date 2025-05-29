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
    # Set the language Portuguese (Brazil) and the first voice available
    # change_voice(engine, lenguage, "VoiceGenderNeuter")  # Change to Portuguese (Brazil) neuter voice
    engine.setProperty('voice', "com.apple.eloquence.pt-BR.Sandy")  # Set to Portuguese (Brazil) voice
    speak(engine, "Olá, este é um teste de conversão de texto em fala.")
    speak(engine, "Como posso ajudá-lo hoje?")
    speak(engine, "Adeus!")
    speak(engine, "Este é um exemplo simples de conversão de texto em fala com Python.")
    speak(engine, "Obrigado por usar este programa.")
    speak(engine, "Tenha um ótimo dia!")
    speak(engine, "Este é um exemplo de biblioteca pyttsx3.")
    speak(engine, "Sinta-se à vontade para modificar o texto conforme necessário.")
    speak(engine, "Este código foi projetado para converter texto em fala.")
    speak(engine, "Você pode usá-lo para várias aplicações.")

    # Set the language English (United States) and the first voice available
    # change_voice(engine, lenguage2, "VoiceGenderNeuter")  # Change to English (United States) neuter voice
    engine.setProperty('voice', "com.apple.voice.compact.en-US.Samantha")  # Set to English (United States) voice
    speak(engine, "Hello, this is a text-to-speech conversion test.")
    speak(engine, "How can I assist you today?")
    speak(engine, "Goodbye!")
    speak(engine, "This is a simple example of text-to-speech conversion with Python.")
    speak(engine, "Thank you for using this program.")
    speak(engine, "Have a great day!")
    speak(engine, "This is a demonstration of the pyttsx3 library.")
    speak(engine, "Feel free to modify the text as needed.")
    speak(engine, "This code is designed to convert text to speech.")
    speak(engine, "You can use it for various applications.")

    
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
    
