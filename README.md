# 🗣️ Text-to-Speech (TTS) App using Kokoro

This is a lightweight Streamlit web application that converts text input into speech using the Kokoro TTS model.

## 🚀 Features

- 🎙️ Text to Speech generation using Kokoro (`hexgrad/Kokoro-82M`)
- 🧠 Phoneme-based synthesis
- 🔊 Listen to generated audio directly on the webpage
- 💻 Easy deployment with Streamlit Cloud

## 🛠️ Setup Instructions

 

```bash
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/text2speech-app.git
cd text2speech-app

### 2. Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt


###4. Run the app locally
streamlit run app.py
