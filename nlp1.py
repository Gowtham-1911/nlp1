
import streamlit as st
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Language options dictionary
languages = {
    "en": "English",
    "hi": "Hindi",
    "fr": "French",
    "es": "Spanish",
    "de": "German"
}

# Streamlit App Title
st.title("Text Translator App")

# Text input for translation
text = st.text_area("Enter text to translate:")

# Dropdown for target language
tgt_lang = st.selectbox("Choose target language:", list(languages.keys()), format_func=lambda x: languages[x])

# Translate button
if st.button("Translate"):
    if text:
        # Detect source language
        detected_lang = translator.detect(text).lang
        detected_lang_name = languages.get(detected_lang, "Unknown Language")

        # Translate text
        translated_text = translator.translate(text, src=detected_lang, dest=tgt_lang).text

        # Output detected language and translated text
        st.write(f"**Detected source language:** {detected_lang_name} ({detected_lang})")
        st.write("**Translated text:**")
        st.write(translated_text)
    else:
        st.warning("Please enter some text to translate.")

