import tkinter as tk
from pytube import YouTube

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        title_label.config(text="Title: " + yt.title)
        views_label.config(text="Views: " + str(yt.views))

        yt_download = yt.streams.get_highest_resolution()
        yt_download.download(output_path='C:/Users/Arnab 2001/Desktop/programming/python(S&A)/Automation/YtVdoDownload')
        download_status.config(text="Download completed successfully!")
    except Exception as e:
        download_status.config(text="An error occurred: " + str(e))

def clear_fields():
    url_entry.delete(0, tk.END)
    title_label.config(text="Title: ")
    views_label.config(text="Views: ")
    download_status.config(text="")

# Create a tkinter window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and configure widgets
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.pack()

title_label = tk.Label(root, text="Title: ")
title_label.pack()

views_label = tk.Label(root, text="Views: ")
views_label.pack()

download_status = tk.Label(root, text="")
download_status.pack()

# Start the tkinter main loop
root.mainloop()
