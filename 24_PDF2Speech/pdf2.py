import PyPDF2 
import pyttsx3
import keyboard

def extract_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def stop_speech():
    pyttsx3.engine.Engine().stop()

text = extract_text("CR OMID Ebrahimi2.pdf")
text_to_speech(text)

keyboard.add_hotkey('ctrl+shift+s', stop_speech)
keyboard.wait()