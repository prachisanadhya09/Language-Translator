
import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator")

st.title("🌐 Language Translator")
st.write("Translate complete sentences and paragraphs.")

text = st.text_area("Enter your text here:")

source = st.selectbox("From Language", ["English", "Hindi"])
target = st.selectbox("To Language", ["Hindi", "English"])

language_codes = {
    "English": "en",
    "Hindi": "hi"
}

if st.button("Translate"):
    if text.strip():
        try:
            translated_text = GoogleTranslator(
                source=language_codes[source],
                target=language_codes[target]
            ).translate(text)

            st.success("Translation Successful!")
            st.text_area("Translated Text:", value=translated_text, height=150)

        except Exception:
            st.error("Translation failed. Please try again.")
    else:
        st.warning("Please enter some text.")
