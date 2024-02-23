import pyaudio
import soundfile
import os
import speech_recognition as sr
from pathlib import Path
import textwrap
from fpdf import FPDF

def convert_mp3_to_pdf(mp3_file_path):
    wav_file_path = "output.wav"

    # Convert MP3 to WAV
    convert_mp3_to_wav(mp3_file_path, wav_file_path)

    # Convert WAV to PDF
    convert_wav_to_pdf(wav_file_path)

    # Delete the WAV file
    os.remove(wav_file_path)

    print("Pdf file saved as: output.pdf")


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

if __name__ == "__main__":
    # Provide the path 
    mp3_file_path = Path(r'C:\Users\PATIL\OneDrive\Desktop\pdf to audio\recources\ali.mp3')

    # Convert MP3 to PDF
    convert_mp3_to_pdf(mp3_file_path)


 