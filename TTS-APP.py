import en_core_web_sm

nlp = en_core_web_sm.load()



import streamlit as st
from kokoro import KPipeline
import soundfile as sf
import os

# Initialize the Kokoro TTS pipeline
@st.cache_resource
def load_pipeline():
    return KPipeline(lang_code='a', repo_id='hexgrad/Kokoro-82M')

pipeline = load_pipeline()

# Streamlit UI
st.title("🗣️ Phoneme-Based Text-to-Speech (TTS) App ")
st.markdown("Convert input text to speech using Kokoro TTS model.")

# Text input
text_input = st.text_area("Enter text to synthesize", "Hello, how are you doing today?")

# Voice selection (use one of the available voices)
voice = st.selectbox("Choose a voice", ["af_heart","af_bella","af_nicole"])  # Add more if supported

# Convert Button
if st.button("Convert to Speech"):
    if text_input.strip():
        generator = pipeline(text_input, voice=voice)
        for i, (_, _, audio) in enumerate(generator):
            file_name = f"output_{i}.wav"
            sf.write(file_name, audio, 24000)
            st.audio(file_name, format="audio/wav", start_time=0)
            st.success(f"✅ Audio generated and played below!")
    else:
        st.warning("Please enter some text to synthesize.")

st.markdown("---")
st.markdown("### 👨‍💻 Created by Prasad Jawadekar")
