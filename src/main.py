import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *   

class mainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        QToolTip.setFont(QFont('Arial', 10))
        
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       

        self.setLabels()
        self.setGeometry(200, 70, 1000, 600)
        self.setWindowTitle('Cloud Manager')  
        self.show()

    def setLabels(self):
        
        vmLabel = QLabel('Virtual Machines', self)
        vmCountLabel = QLabel('10', self)
        
        vmLabel.setGeometry(300, 200, 100, 100)
        vmCountLabel.setGeometry(300, 300, 100, 100)       

if __name__ == '__main__':
    
    mainApp = QApplication(sys.argv)
    mv = mainWindow()
    
    sys.exit(mainApp.exec_())