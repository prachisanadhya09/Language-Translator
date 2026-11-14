import streamlit as st
import requests

st.title("🌐 Language Translator")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}

common = {
    ("how are you?", "English", "Hindi"): "आप कैसे हैं?",
    ("how are you", "English", "Hindi"): "आप कैसे हैं?",
    ("i am fine", "English", "Hindi"): "मैं ठीक हूँ।",
    ("hello", "English", "Hindi"): "नमस्ते",
    ("thank you", "English", "Hindi"): "धन्यवाद",
    ("good morning", "English", "Hindi"): "सुप्रभात",
}

text = st.text_area("Enter your text here:")

source = st.selectbox("From language", list(languages.keys()))
target = st.selectbox("To language", list(languages.keys()))

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text.")
    elif source == target:
        st.warning("Please select different languages.")
    else:
        key = (text.strip().lower(), source, target)

        if key in common:
            translated = common[key]
            st.success("Translation:")
            st.write(translated)
            st.code(translated)
        else:
            try:
                response = requests.get(
                    "https://api.mymemory.translated.net/get",
                    params={
                        "q": text,
                        "langpair": f"{languages[source]}|{languages[target]}"
                    },
                    timeout=20
                )
                data = response.json()

                if data.get("responseStatus") == 200:
                    translated = data["responseData"]["translatedText"]
                    st.success("Translation:")
                    st.write(translated)
                    st.code(translated)
                else:
                    st.error("Translation unavailable. Try again later.")

            except Exception:
                st.error("Translation failed. Please try again.")
