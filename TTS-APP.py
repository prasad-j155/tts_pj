import streamlit as st
from huggingface_hub import InferenceClient

# Title
st.title("🎤 PJ PRODUCTIONS TTS(Text to Speech) App")

# Load API key securely from Streamlit secrets
api_key = st.secrets["HF_API_KEY"]


# Initialize the inference client
client = InferenceClient(
    provider="fal-ai",
    api_key=api_key,
)

# Text input
text_input = st.text_area("Enter text to synthesize:", "The answer to the universe is 42")

# Button to synthesize
if st.button("Generate Speech"):
    with st.spinner("Generating..."):
        try:
            # Get audio bytes from Hugging Face model
            audio_bytes = client.text_to_speech(
                text_input,
                model="hexgrad/Kokoro-82M",
            )

            # Play audio
            st.audio(audio_bytes, format="audio/wav")
        except Exception as e:
            st.error(f"Error generating audio: {e}")
