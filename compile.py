import PyInstaller.__main__

PyInstaller.__main__.run(
    [
        "-F",
        "src/main.py",
        "--clean",
        "--onefile",
        "--noconsole",
        "--noconfirm",
        "--icon",
        "icons/whistle_of_wind.png",
        "--name",
        "Whistle of Wind",
    ]
)