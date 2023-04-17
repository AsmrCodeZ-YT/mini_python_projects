import pyttsx3

book = open(r"audioLabrary/readit.text")
book_t = book.readlines()
engine = pyttsx3.init()

for ib in book_t:
    engine.say(ib)
    engine.runAndWait()

