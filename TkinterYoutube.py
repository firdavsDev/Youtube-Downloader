from tkinter import *
from pytube import YouTube
import os
root = Tk()
# geometry
root.geometry('600x200')
root.title('Youtube Downloader | Beta')
root.resizable(False,False)

# Label for text
label_1 = Label(root,text='Enter youtube link',font=('bold',20))
label_1.place(x=170,y=20)

#label 2
label_2 = Label(root,text='Youtube video dowloader By DjangoCoder!')
label_2.place(x=150,y=150)

# entry for link
my_link = StringVar()
link = Entry(root,width=60,textvariable=my_link)
link.place(x=140,y=80)

l = Label(root, text='')
l.pack(side=TOP)

# func for download
def Download():
    x = str(my_link.get())
    try:
        if str(x)!=0 and len(str(x))==28 and str(x)[:16]=='https://youtu.be':
            yvideo = YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            if not os.path.exists('./Youtube'):
                os.makedirs('./Youtube')
            yvideo.download('./Youtube')
            l.config(text=str('Video Downloaded! in Youtube folder'),bg='green')
        else:
            l.config(text=str('Errored'),bg='red')
    except Exception as e:
        l.config(text=e,bg='red')

#button 
Button(root,text='Download',width=20,bg='green',fg='white',command=Download).place(x=220,y=120)
 # works, Like and comment 

# python file to change .exe file - pip install pyinstaller then write to cmd or powershell pyinstaller -F -w {filepath}
root.mainloop()