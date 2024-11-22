import os


def list_folders(directory):
    return [
        name
        for name in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, name))
    ]


def package_to_name(s):
    words = s.split("_")
    transformed = " ".join(
        word.lower() if i != 0 else word.capitalize() for i, word in enumerate(words)
    )
    return transformed


def name_to_package(s):
    words = s.split()
    transformed = "_".join(word.lower() for word in words)
    return transformed
