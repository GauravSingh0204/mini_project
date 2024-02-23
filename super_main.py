import os
import PyPDF4
import pyaudio
import textwrap
import soundfile
import tkinter as tk
from fpdf import FPDF
from gtts import gTTS
from pathlib import Path
from tkinter import filedialog
import speech_recognition as sr



#import sys  # Import sys module to access command-line arguments

def convert_pdf_to_audio(pdf_path):
    try:
        # Open file Path
        pdf_File = open(pdf_path, 'rb') 

        # Create PDF Reader Object
        pdf_Reader = PyPDF4.PdfFileReader(pdf_File)
        count = pdf_Reader.numPages  # counts number of pages in pdf
        textList = []

        # Extracting text data from each page of the pdf file
        for i in range(count):
            try:
                page = pdf_Reader.getPage(i)    
                textList.append(page.extractText())
            except:
                pass

        # Converting multiline text to single line text
        textString = " ".join(textList)

        def text_to_audio(paragraph, language='en', output_file='output.mp3'):
            tts = gTTS(text=paragraph, lang=language, slow=False)
            tts.save(output_file)
            return output_file

        if __name__ == "__main__":
            output_file = text_to_audio(textString)
            print(f"Audio file saved as: {output_file}")

    except FileNotFoundError:
        print(f"Error: File not found at path {pdf_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def convert_mp3_to_pdf(mp3_file_path):
    wav_file_path = "output.wav"

    # Convert MP3 to WAV
    convert_mp3_to_wav(mp3_file_path, wav_file_path)

    # Convert WAV to PDF
    convert_wav_to_pdf(wav_file_path)

    print("Pdf file saved as: output.pdf")

    # Delete the WAV file
    os.remove(wav_file_path)

def convert_mp3_to_wav(mp3_file, wav_file):
    p = pyaudio.PyAudio()

    # Open the MP3 file
    with soundfile.SoundFile(mp3_file, 'rb') as mp3:
        # Read the MP3 file
        mp3_data = mp3.read(dtype='int16')
        
        # Save the data as WAV file
        soundfile.write(wav_file, mp3_data, samplerate=mp3.samplerate)

def convert_wav_to_pdf(wav_file):
    recognizer = sr.Recognizer()

    # Open the WAV file
    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    
    # Create PDF
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output("output.pdf", 'F')

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

audio_button = tk.Button(frame, text="Convert Audio to pdf", command=browse_audio, height=3, width=20)
audio_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
