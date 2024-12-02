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
        "icons/settings_input_antenna_24dp_0000F5_FILL0_wght400_GRAD0_opsz24.png",
        "--name",
        "Whistle of Wind",
    ]
)