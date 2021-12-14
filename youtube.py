# import
# pip install pytube
from pytube import YouTube
#https://youtu.be/PMNZs99TPes
def Download(x):
    try:
        if str(x)!=0 and len(str(x))==28 and str(x)[:16]=='https://youtu.be':
            yvideo = YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            yvideo.download('FolderPath')
    except Exception as e:
        print(e)

#call func
x = str(input('Youtube Link'))
Download(x)

# Work well next lesson we connect to Tkinter Like and comment!