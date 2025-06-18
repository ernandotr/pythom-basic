from langdetect import detect

text = input("Enter text to detect language: ")

try:
    language = detect(text)
    print(f"The detected language is: {language}")
except Exception as e:
    print(f"An error occurred while detecting language: {e}")
