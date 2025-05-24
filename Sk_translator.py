# Shahzaib Khan

import tkinter as tk
from tkinter import messagebox, ttk
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from datetime import datetime
from playsound import playsound
import os

# Supported languages
LANGUAGES = {
    "Urdu": "ur",
    "Arabic": "ar",
    "Chinese": "zh-cn",
    "English": "en",
    "Japanese": "ja",
    "German": "de"
}

# Function to log translation
def log_translation(input_lang, target_lang, original, translated):
    with open("translations.log", "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now()}] [{input_lang} → {target_lang}]\n")
        log.write(f"Original: {original}\n")
        log.write(f"Translated: {translated}\n\n")

# Speech recognition
def recognize_speech(lang_code):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        status_label.config(text="🎤 Listening...")
        spinner.place(x=220, y=135)
        spinner.start()
        app.update()
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    spinner.stop()
    spinner.place_forget()
    status_label.config(text="🔁 Processing...")
    app.update()
    try:
        return recognizer.recognize_google(audio, language=lang_code)
    except Exception as e:
        messagebox.showerror("Error", f"Speech recognition failed: {e}")
        return None

# Translate and speak
def translate_to(target_lang_name):
    input_lang_name = input_lang_var.get()
    input_lang_code = LANGUAGES[input_lang_name]
    target_lang_code = LANGUAGES[target_lang_name]

    original_text = recognize_speech(input_lang_code)
    if not original_text:
        return

    translator = Translator()
    translated = translator.translate(original_text, src=input_lang_code, dest=target_lang_code).text

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, f"Original ({input_lang_name}): {original_text}\n")
    output_box.insert(tk.END, f"Translated ({target_lang_name}): {translated}\n")

    try:
        tts = gTTS(text=translated, lang=target_lang_code)
        tts.save("speech.mp3")
        playsound("speech.mp3")
        os.remove("speech.mp3")
    except Exception as e:
        messagebox.showwarning("Speech Error", f"Speech playback failed: {e}")

    log_translation(input_lang_name, target_lang_name, original_text, translated)
    status_label.config(text="✅ Translation complete")

# GUI setup
app = tk.Tk()
app.title("🎙️ Sk's Speech Translator")
app.geometry("560x520")
app.config(bg="#2E294E")

tk.Label(app, text="🎙️ Sk's Speech Translator", font=("Helvetica", 16, "bold"),
         bg="#2E294E", fg="#0EF0F8").pack(pady=10)

# Input language toggle
input_lang_var = tk.StringVar(value="English")

tk.Label(app, text="Select Input Language:", font=("Helvetica", 12),
         bg="#2E294E", fg="#E0E0E0").pack()

toggle_frame = tk.Frame(app, bg="#2E294E")
toggle_frame.pack(pady=5)

for lang in ["English", "Urdu"]:
    tk.Radiobutton(toggle_frame, text=lang, variable=input_lang_var, value=lang,
                   font=("Helvetica", 11), bg="#2E294E", fg="#E0E0E0",
                   selectcolor="#4A4E69", activebackground="#9D32FA").pack(side=tk.LEFT, padx=10)

# Spinner (loading wheel)
spinner = ttk.Progressbar(app, mode='indeterminate', length=120)
spinner.stop()
spinner.place_forget()

# Target language buttons
tk.Label(app, text="Translate To:", font=("Helvetica", 12),
         bg="#2E294E", fg="#E0E0E0").pack(pady=5)

target_frame = tk.Frame(app, bg="#2E294E")
target_frame.pack()

for lang in LANGUAGES:
    tk.Button(target_frame, text=lang, width=16, font=("Helvetica", 11),
              bg="#4A4E69", fg="#E0E0E0", activebackground="#6C5B7B",
              command=lambda l=lang: translate_to(l)).pack(pady=4)

# Output box
output_box = tk.Text(app, height=8, width=60, font=("Courier", 10),
                     bg="#22223B", fg="#E0E0E0", insertbackground="#E0E0E0")
output_box.pack(pady=10)

# Status label
status_label = tk.Label(app, text="Ready", bg="#2E294E", fg="#E0E0E0", font=("Helvetica", 10))
status_label.pack(pady=5)

app.mainloop()
