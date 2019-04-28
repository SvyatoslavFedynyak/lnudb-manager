import UI.dataInfo
from PyQt5 import QtWidgets

class dataWindow(QtWidgets.QMainWindow, UI.dataInfo.Ui_dataInfo):
    def __init__(self, parent=None):
        super(dataWindow, self).__init__(parent)
        self.setupUi(self)

