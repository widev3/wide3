# import importlib
# import os
# import json
# import sys
# from os.path import dirname
# from Config import Config
# from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QMessageBox

# config = Config()


# def start_a_module(module):
#     dynamic_module = importlib.import_module(f"{module}.view.view")
#     dynamic_function = getattr(dynamic_module, "view")
#     dynamic_function(config.data[module] if module in config.data else None)
#     print("ciao")


# class DynamicButtonPopup(QDialog):
#     def __init__(self, folders_config):
#         super().__init__()

#         self.setWindowTitle("Dynamic Button Popup")
#         self.setGeometry(100, 100, 300, 200)

#         layout = QVBoxLayout()

#         for folder_config in folders_config:
#             button = QPushButton(folders_config[folder_config]["name"], self)
#             button.clicked.connect(lambda x: start_a_module(folder_config))
#             layout.addWidget(button)

#         self.setLayout(layout)


# if __name__ == "__main__":
#     startup = ""
#     if "startup" in config.data:
#         startup = config.data["startup"]

#     if startup:
#         start_a_module(startup)
#     else:
#         # folders = list(
#         #     filter(
#         #         lambda x: not x.startswith("__"), next(os.walk(dirname(__file__)))[1]
#         #     )
#         # )

#         # folders_config = {}
#         # for folder in folders:
#         #     with open(f"{folder}/config.json", "r") as file:
#         #         folders_config[folder] = json.load(file)

#         # app = QApplication(sys.argv)
#         # dialog = DynamicButtonPopup(folders_config)
#         # dialog.exec_()
#         # sys.exit(app.exec_())
