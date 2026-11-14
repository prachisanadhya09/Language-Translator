
import streamlit as st

st.title("🌐 Language Translator")

text = st.text_area("Enter your text here:")

translations = {
    "hello": "नमस्ते",
    "how are you": "आप कैसे हैं?",
    "good morning": "सुप्रभात",
    "thank you": "धन्यवाद",
    
}

if st.button("Translate"):
    word = text.strip().lower()
    if word in translations:

        st.success(translations[word])
    else:
        st.warning("Translation not available.")
