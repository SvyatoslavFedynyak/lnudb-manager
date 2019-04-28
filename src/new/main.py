import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import modules.dataInfo, modules.mainWindow

if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    window = modules.mainWindow.mainWindow()
    #window = modules.dataInfo.dataInfoDialog()
    window.show()
    mainApp.exec_()