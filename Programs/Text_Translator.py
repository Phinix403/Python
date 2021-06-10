# Install Translator Package - pip install translate

from translate import Translator

from_lang = input("\nFrom Lang: ")
to_lang = input("To Lang: ")
text = input("Enter Text: ")

translator = Translator(from_lang=from_lang, to_lang=to_lang).translate(text)

print(f"\nGiven Text: {text} \nTranslated Text: {translator}\n")