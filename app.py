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

text = st.text_area("Enter your text here:")

source = st.selectbox("From language", list(languages.keys()))
target = st.selectbox("To language", list(languages.keys()))

if st.button("Translate"):
    if text.strip():
        if source == target:
            st.warning("Please select different languages.")
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
                if source == "English" and target == "Hindi":
    if text.strip().lower() in ["how are you", "how are you?"]:
        st.success("आप कैसे हैं?")
        st.stop()

                if data.get("responseStatus") == 200:
                    translated = data["responseData"]["translatedText"]
                    st.success("Translation:")
                    st.write(translated)
                    st.code(translated)
                else:
                    st.error("Translation service is unavailable. Try later.")

            except Exception as e:
                st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text.")
