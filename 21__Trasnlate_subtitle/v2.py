from progress.bar import Bar
from time import sleep
from deep_translator import GoogleTranslator
from pathlib import Path

File_ = input("SubTitle: ")

# p = Path("./sub.srt")

with open("ex22ort.srt","w",encoding="utf-8") as result:
    with Bar('Processing...',fill='@') as bar: # bar procsse
        with open(File_,"r") as f:
            sen = f.readlines()
            len_ = len(sen)
            for i in range(6,len_,4):
                all_text = sen[i].strip()
                translated = GoogleTranslator(source='auto', target='fa').translate(all_text)  
                sen[i] = f"{translated}\n"
                bar.next()
                
        # wtire
        for i in range(len_):
            result.write(sen[i]) 
