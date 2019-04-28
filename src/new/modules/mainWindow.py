import UI.mwDesign
from PyQt5 import QtWidgets
import modules.dataInfo

class mainWindow(QtWidgets.QMainWindow, UI.mwDesign.Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.vmButton.clicked.connect(lambda: self.moreInfoClick('vmButton'))
        self.dialog = modules.dataInfo.dataWindow(self)

    def moreInfoClick(self, btnName):
        if btnName == 'vmButton':
            self.dataDialog = modules.dataInfo.dataWindow(self)
            self.dataDialog.show()
