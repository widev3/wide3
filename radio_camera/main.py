import os
import tkinter as tk
from tkinter import filedialog


def split_file_by_empty_lines(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()
        chunks = []
        current_chunk = []

        for line in lines:
            if line.strip() == "":
                if current_chunk:
                    chunks.append(current_chunk)
                    current_chunk = []
            else:
                current_chunk.append(line)

        if current_chunk:
            chunks.append(current_chunk)

    return chunks


if __name__ == "__main__":
    from csv_reader.Config import Config

    config = Config()
    filename = ""
    if "filename" in config.data:
        if config.data["filename"]:
            if os.path.isfile(config.data["filename"]):
                filename = config.data["filename"]

    if not filename:
        window = tk.Tk()
        window.wm_attributes("-topmost", 1)
        window.withdraw()
        filename = filedialog.askopenfilename(
            parent=window,
            title="Select A File",
            filetypes=(("csv", "*.csv"), ("Text files", "*.txt")),
        )

    file = split_file_by_empty_lines(filename)

    from csv_reader.properties import properties

    pr = properties(file[0], config)

    from csv_reader.frequencies import frequencies

    fr = frequencies(file[1], config)

    from csv_reader.spectrogram import spectrogram

    sp = spectrogram(file[2], config)

    from radio_camera.view import main_view

    main_view(pr, fr, sp, config)
