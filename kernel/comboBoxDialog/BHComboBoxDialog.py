class BHComboBoxDialog:
    def __init__(self, ui, dialog, args=None):
        self.ui = ui
        self.dialog = dialog
        self.ui.comboBox.currentIndexChanged.connect(self.index_changed)
        if args:
            self.ui.comboBox.addItems(args)

    def index_changed(self, index):
        self.dialog.accept()
        self.index = index
        self.text = self.ui.comboBox.itemText(index)
