import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌐 Language Translator")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}

text = st.text_area("Enter your text here:")

source = st.selectbox("From language", list(languages.keys()))
target = st.selectbox("To language", list(languages.keys()))

if st.button("Translate"):
    if text.strip():
        try:
            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.success("Translation:")
            st.write(translated)

            st.code(translated)

        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text.")
