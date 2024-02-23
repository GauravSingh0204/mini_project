# pdf_to_audio.py

# Importing Libraries
from gtts import gTTS
import PyPDF4
from pathlib import Path

def convert_pdf_to_audio(pdf_path):
    
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

    #print(textString)

    output_file = text_to_audio(textString)
    print(f"Audio file saved as: {output_file}")

def text_to_audio(paragraph, language='en', output_file='output.mp3'):
            tts = gTTS(text=paragraph, lang=language, slow=False)
            tts.save(output_file)
            return output_file