from deep_translator import GoogleTranslator
import os 

translator = GoogleTranslator()
lags_dict = translator.get_supported_languages(as_dict=True)
allKey = list(lags_dict.keys())
allValues = list(lags_dict.values())

# description
print("number of lang support : " ,len(lags_dict.keys()))
for num in range(len(lags_dict.keys())):
    print(num,"==",allKey[num],"===>" ,allValues[num])

#inputs 
fileInput = input("Give me ur SubTitle :: ")
sourceInput = input("translate from [lang] :: ")
TargetInput = input("translate to [lang] :: ")
new_file_subtitle = f"{TargetInput}_{os.path.basename(fileInput)}"


with open(new_file_subtitle,"w" ,encoding="utf-8") as sub:
    with open(fileInput,"r" ,encoding="utf-8") as f:
           
        all_subtitles = f.readlines()
        sent_extract = all_subtitles[2::4]
         
        for i in range(len(sent_extract)):
            sentence = sent_extract[i]
            translate = GoogleTranslator(source=sourceInput , target=TargetInput).translate(sentence)
            sent_extract[i] = f"{translate}\n"
            
            print(f"{i}/{len(sent_extract)}")
            
            
        all_subtitles[2::4] = sent_extract
        # print(all_subtitles)
        sub.writelines(all_subtitles)
        print("Done!")