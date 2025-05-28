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
    change_voice(engine, "nl_BE", "VoiceGenderFemale")
    engine.say("Hello World")
    engine.runAndWait()
    # speak("Olá, este é um teste de conversão de texto em fala.")
    # speak("Como posso ajudá-lo hoje?")
    # speak("Adeus!")
    # speak("Este é um exemplo simples de conversão de texto em fala usando Python.")
    # speak("Obrigado por usar este programa.")
    # speak("Tenha um ótimo dia!")
    # speak("Esta é uma demonstração da biblioteca pyttsx3.")
    # speak("Sinta-se à vontade para modificar o texto conforme necessário.")
    # speak("Este código foi projetado para converter texto em fala.")
    # speak("Você pode usar isso para várias aplicações.")

    # speak("Hello, this is a text-to-speech test.")
    # speak("How can I assist you today?")
    # speak("Goodbye!")
    # speak("This is a simple text-to-speech example using Python.")
    # speak("Thank you for using this program.")
    # speak("Have a great day!")
    # speak("This is a demonstration of the pyttsx3 library.")
    # speak("Feel free to modify the text as needed.")
    # speak("This code is designed to convert text to speech.")
    # speak("You can use this for various applications.")

    engine.setProperty('voice', "com.apple.voice.compact.fr-FR.Thomas")  # Set to the first voice
    speak(engine, "Bonjour, ceci est un test de conversion de texte en parole.")
    # speak("Comment puis-je vous aider aujourd'hui ?")
    # speak("Au revoir !")
    # speak("Ceci est un exemple simple de conversion de texte en parole avec Python.")
    # speak("Merci d'avoir utilisé ce programme.")
    # speak("Passez une excellente journée !")
    # speak("Ceci est une démonstration de la bibliothèque pyttsx3.")
    # speak("N'hésitez pas à modifier le texte selon vos besoins.")
    # speak("Ce code est conçu pour convertir du texte en parole.")
    # speak("Vous pouvez l'utiliser pour diverses applications.")
    
