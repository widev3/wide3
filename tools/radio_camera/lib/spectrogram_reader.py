from radio_camera.lib.properties import properties
from radio_camera.lib.frequencies import frequencies
from radio_camera.lib.spectrogram import spectrogram


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


def reader(filename, config):
    file = split_file_by_empty_lines(filename)
    pr = properties(file[0], config)
    fr = frequencies(file[1], config)
    sp = spectrogram(file[2], config)

    return pr, fr, sp
