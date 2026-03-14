import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pytubefix import YouTube

# ------------------------
# Functions
# ------------------------
def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        save_path_var.set(folder_selected)

def download_audio():
    url = url_entry.get().strip()
    folder = save_path_var.get().strip()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL!")
        return
    if not folder:
        messagebox.showerror("Error", "Please select a folder to save the audio!")
        return

    # Clean URL
    if "?" in url:
        url = url.split("?")[0]

    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        file_path = audio_stream.download(output_path=folder)

        messagebox.showinfo("Success", f"Downloaded '{yt.title}' to:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# ------------------------
# GUI Setup
# ------------------------
root = tk.Tk()
root.title("YouTube Audio Downloader")
root.geometry("500x200")
root.resizable(False, False)

# URL Entry
tk.Label(root, text="YouTube URL:").pack(pady=(10,0))
url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

# Save Folder
tk.Label(root, text="Save to folder:").pack(pady=(10,0))
save_path_var = tk.StringVar()
save_entry = tk.Entry(root, textvariable=save_path_var, width=45)
save_entry.pack(side=tk.LEFT, padx=(20,0))
tk.Button(root, text="Browse", command=browse_folder).pack(side=tk.LEFT, padx=10)

# Download Button
tk.Button(root, text="Download Audio (.m4a)", command=download_audio, bg="green", fg="white").pack(pady=20)

root.mainloop()
