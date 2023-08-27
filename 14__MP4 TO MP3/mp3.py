import moviepy
import moviepy.editor


inpt = input("give me ur file ::::: ")

video = moviepy.editor.VideoFileClip(inpt)

audio = video.audio
audio.write_audiofile(f"{inpt}.mp3")

