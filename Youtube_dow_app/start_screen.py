import os
from tkinter import Button, Entry, font, filedialog, Label, NW
from canvas1 import root, frame
from pytube import YouTube
from PIL import ImageTk, Image
from helprers import clean_screen


def app_icon():
    path = 'youtube_button2.png'
    img = ImageTk.PhotoImage(Image.open(path))
    images.append(img)
    frame.create_image(300, 150, image=img)


def render_start():
    app_icon()
    myFont = font.Font(weight="bold")
    start_button = Button(
        root,
        text='Start',
        bg='red',
        fg='#EDF5FC',
        borderwidth=0,
        width=7,
        height=2,
        command=render_download
    )
    start_button['font'] = myFont

    frame.create_text(300, 250, text="Place your link:", font=("arial", 24), fill='#272D2D')
    frame.create_window(300, 300, window=link_box)
    frame.create_window(550, 300, window=start_button)


def render_download():
    clean_screen()
    try:
        myfont2 = font.Font(weight="bold")
        audio_button = Button(
            root,
            text='Audio',
            bg='#23CE6B',
            fg='#EDF5FC',
            borderwidth=0,
            width=7,
            height=2,
            command=download_audio
        )
        audio_button['font'] = myfont2

        video_button = Button(
            root,
            text='Video',
            bg='#23CE6B',
            fg='#EDF5FC',
            borderwidth=0,
            width=7,
            height=2,
            command=download_video

        )
        video_button['font'] = myfont2
        frame.create_window(600, 400, window=audio_button, tag='error')
        frame.create_window(600, 500, window=video_button, tag='error')

        yt = YouTube(link_box.get())
        title_text = f"{yt.title}\nViews {yt.views}"
        frame.create_text(300, 400, text=title_text, font=("arial", 14), fill='#272D2D', tag='error')
        #frame.create_text(300, 450, text=, font=("arial", 14), fill='#272D2D')
    except:
        clean_screen()
        frame.create_text(300, 400, text="Invalid link!!!", font=("arial", 14), fill='red', tag='error')



def download_video():
    yt = YouTube(link_box.get())
    video = yt.streams.get_highest_resolution()
    video.download()


def download_audio():
    yt = YouTube(link_box.get())
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)



link_box = Entry(root, font=("arial", 24), bd=0, background='#EDF5FC')

images = []