import langdetect 

def detect_language(text):
    try:
        language = langdetect.detect(text)
        return language
    except langdetect.lang_detect_exception.LangDetectException:
        return "Could not detect language"
# Example usage
text = "Hello, how are you?"
language = detect_language(text)
print(f"The detected language is: {language}")
text = "Hola, ¿cómo estás?"
language = detect_language(text)
print(f"The detected language is: {language}")
text = "Bonjour, comment ça va?"
language = detect_language(text)
print(f"The detected language is: {language}")
text = "你好，你怎么样？"
language = detect_language(text)
print(f"The detected language is: {language}")
text = "Привет, как дела?"
language = detect_language(text)
print(f"The detected language is: {language}")
text = "こんにちは お元気ですか？"
language = detect_language(text)
print(f"The detected language is: {language}")

