import tkinter as tk
from tkinter import filedialog

import os
from audio_to_pdf import convert_mp3_to_pdf
from pdf_to_audio import convert_pdf_to_audio


def browse_pdf():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        convert_pdf_to_audio(pdf_path)

def browse_audio():
    audio_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3;*.wav")])
    if audio_path:
        convert_mp3_to_pdf(audio_path)

# Create the main window
window = tk.Tk()
window.title("PDF to Audio and Audio to PDF converter")
window.geometry('700x300')
window.config(bg='LightBlue1')

# Create a frame to hold the buttons and center it
frame = tk.Frame(window, bg='LightBlue1')
frame.place(relx=0.5, rely=0.5, anchor='center')

# Create buttons
pdf_button = tk.Button(frame, text="Convert PDF to Audio", command=browse_pdf, height=3, width=20)
pdf_button.pack(pady=10)

audio_button = tk.Button(frame, text="Convert Audio to Text", command=browse_audio, height=3, width=20)
audio_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
