
import streamlit as st

st.title("🌐 Language Translator")

text = st.text_area("Enter your text here:")

from_language = st.selectbox(
    "From Language",
    ["English", "Hindi"]
)

to_language = st.selectbox(
    "To Language",
    ["Hindi", "English"]
)

english_to_hindi = {
    "hello": "नमस्ते",
    "how are you": "आप कैसे हैं?",
    "good morning": "सुप्रभात",
    "thank you": "धन्यवाद",
    "good night": "शुभ रात्रि",
    "welcome": "स्वागत है",
    "goodbye": "अलविदा",
    "i am fine": "मैं ठीक हूँ"
}

hindi_to_english = {
    "नमस्ते": "Hello",
    "आप कैसे हैं?": "How are you?",
    "सुप्रभात": "Good morning",
    "धन्यवाद": "Thank you",
    "शुभ रात्रि": "Good night",
    "स्वागत है": "Welcome",
    "अलविदा": "Goodbye",
    "मैं ठीक हूँ": "I am fine"
}

if st.button("Translate"):
    word = text.strip().lower()

    if not word:
        st.warning("Please enter some text.")

    elif from_language == to_language:
        st.warning("Please select different languages.")

    elif from_language == "English":
        result = english_to_hindi.get(word)

        if result:
            st.success(result)
        else:
            st.warning("Translation not available.")

    else:
        result = hindi_to_english.get(text.strip())

        if result:
            st.success(result)
        else:
            st.warning("Translation not available.")

