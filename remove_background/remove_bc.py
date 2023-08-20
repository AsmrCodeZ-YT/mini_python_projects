from rembg import remove
import os

from pathlib import Path

if "remove" not in os.listdir():
    os.mkdir("remove")
else:
    print("exist")

input_path = input("Give me path :::  ")
input_path_2 = Path(input_path).stem

output_path = f"remove/{input_path_2}.jpg"

with open(input_path , "rb") as i:
    with open(output_path ,"wb") as o:
        input_ = i.read()
        output = remove(input_)
        o.write(output)