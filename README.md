# 🎙️ Sk's Speech Translator

A Python-based GUI application that recognizes speech in **English** or **Urdu** and translates it into **Urdu**, **Arabic**, **Chinese**, **Japanese**, or **German**.  
It features voice playback of translated text, a modern dark purple/grey interface, a toggle to select input language, a live spinner while listening, and logs all translations to a file.

---

## Features

- Speech recognition for English and Urdu input  
- Translation to 5 languages: Urdu, Arabic, Chinese, Japanese, German  
- Text-to-speech playback of translated output  
- Dark-themed, user-friendly Tkinter GUI  
- Input language toggle via radio buttons  
- Spinner animation while listening for input  
- Logs translations with timestamps to `translations.log`  
- Error handling with popup alerts

---

## Demo Screenshot

![image](https://github.com/user-attachments/assets/d05391ca-6b37-4eb9-a5a4-03ee6a181039)


---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/sk-speech-translator.git
   cd sk-speech-translator
   
2. (Recommended) Create a virtual environment:

python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
Install dependencies:

pip install -r requirements.txt

3. Usage
Run the translator GUI:

bash
python Sk_translator.py
Select your input language (English or Urdu) using the radio buttons.

Click any target language button to start speech input.

Speak clearly; the app will detect your speech and translate it.

The translated text will display and be spoken aloud.

Translations are logged in translations.log.

File Structure

speech_translator/
├── Sk_translator.py       # Main Python GUI app
├── requirements.txt        # Python dependencies
└── translations.log        # Translation history log (auto-generated)
Dependencies
SpeechRecognition

googletrans (4.0.0-rc1)

gTTS

playsound

Tkinter (usually pre-installed with Python)

Notes
Requires an active internet connection for Google Translate API and gTTS.

Microphone access is necessary for speech input.

Acknowledgments
Powered by Google Translate and gTTS services

Inspired by the need for accessible multilingual speech translation tools

Developed by Sk










