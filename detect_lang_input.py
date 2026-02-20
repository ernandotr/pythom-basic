from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0

def detect_language(text):
    try:
        language = detect(text)
        return language
    except Exception as e:
        return f"Error detecting language: {str(e)}"
# Example usage
if __name__ == "__main__":
    text = input("Enter text to detect language: ")
    language = detect_language(text)
    print(f"The detected language is: {language}")
    