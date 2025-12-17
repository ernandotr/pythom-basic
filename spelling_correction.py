# spelling_correction.py
# pip install textblob

from textblob import TextBlob

blob = TextBlob("I havv goood speling")
corrected_blob = blob.correct()
print("Original Text: ", blob)
print("Corrected Text:", corrected_blob)

