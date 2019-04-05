import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *   

class mainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):   

        self.setLabels()
        self.setButtons()
        self.setGeometry(200, 70, 950, 600)
        self.setWindowTitle('Cloud Manager')  
        self.show()

    def setLabels(self):
        
        #Init
        dashboardLabel = QLabel('Dashboard', self)
        dashboardLabel.setGeometry(400, 10, 200, 100)
        dashboardLabel.setFont(QFont('Arial', 28))

        #VM
        vmLabel = QLabel('Virtual Machines', self)
        vmLabel.setGeometry(150, 100, 200, 100)
        vmLabel.setFont(QFont('Arial', 20))
        vmCountLabel = QLabel('Count', self)
        vmCountLabel.setGeometry(150, 140, 100, 100)
        vmCountLabel.setFont(QFont('Arial', 16))
        vmCount = QLabel('323', self)
        vmCount.setGeometry(250, 140, 100, 100)
        vmCount.setFont(QFont('Arial', 16))

        
        #LAN
        lanLabel = QLabel('Virtual LAN', self)
        lanLabel.setGeometry(150, 270, 200, 100)
        lanLabel.setFont(QFont('Arial', 20))
        lanCountLabel = QLabel('Count', self)
        lanCountLabel.setGeometry(150, 310, 100, 100)
        lanCountLabel.setFont(QFont('Arial', 16))
        lanCount = QLabel('54', self)
        lanCount.setGeometry(250, 310, 100, 100)
        lanCount.setFont(QFont('Arial', 16))

        #Hosts
        hostsLabel = QLabel('Hosts', self)
        hostsLabel.setGeometry(650, 270, 200, 100)
        hostsLabel.setFont(QFont('Arial', 20))
        hostsCountLabel = QLabel('Count', self)
        hostsCountLabel.setGeometry(650, 310, 100, 100)
        hostsCountLabel.setFont(QFont('Arial', 16))
        hostsCount = QLabel('34', self)
        hostsCount.setGeometry(750, 310, 100, 100)
        hostsCount.setFont(QFont('Arial', 16))



        #Images
        imagesLabel = QLabel('Images', self)
        imagesLabel.setGeometry(650, 100, 200, 100)
        imagesLabel.setFont(QFont('Arial', 20))
        imagesCountLabel = QLabel('Count', self)
        imagesCountLabel.setGeometry(650, 140, 100, 100)
        imagesCountLabel.setFont(QFont('Arial', 16))
        imagesCount = QLabel('11', self)
        imagesCount.setGeometry(750, 140, 100, 100)
        imagesCount.setFont(QFont('Arial', 16))


        #Datastores
        datastoresLabel = QLabel('Datastores', self)
        datastoresLabel.setGeometry(400, 400, 200, 100)
        datastoresLabel.setFont(QFont('Arial', 20))
        datastoresCountLabel = QLabel('Count', self)
        datastoresCountLabel.setGeometry(400, 440, 100, 100)
        datastoresCountLabel.setFont(QFont('Arial', 16))
        datastoresCount = QLabel('66', self) 
        datastoresCount.setGeometry(500, 440, 100, 100)
        datastoresCount.setFont(QFont('Arial', 16))

    def setButtons(self):

        #VM
        vmDataBtn = QPushButton('Data', self)
        vmDataBtn.setGeometry(150, 220, 80, 40)
        vmDataBtn.setFont(QFont('Arial, 16'))
        vmAddBtn = QPushButton('Add', self)
        vmAddBtn.setGeometry(250, 220, 80, 40)
        vmAddBtn.setFont(QFont('Arial, 16'))

        #LAN 
        lanDataBtn = QPushButton('Data', self)
        lanDataBtn.setGeometry(150, 390, 80, 40)
        lanDataBtn.setFont(QFont('Arial, 16'))
        lanAddBtn = QPushButton('Add', self)
        lanAddBtn.setGeometry(250, 390, 80, 40)
        lanAddBtn.setFont(QFont('Arial, 16'))
        
        #Hosts
        hostsDataBtn = QPushButton('Data', self)
        hostsDataBtn.setGeometry(650, 390, 80, 40)
        hostsDataBtn.setFont(QFont('Arial, 16'))
        hostsAddBtn = QPushButton('Add', self)
        hostsAddBtn.setGeometry(750, 390, 80, 40)
        hostsAddBtn.setFont(QFont('Arial, 16'))

        #Images
        imagesDataBtn = QPushButton('Data', self)
        imagesDataBtn.setGeometry(650, 220, 80, 40)
        imagesDataBtn.setFont(QFont('Arial, 16'))
        imagesAddBtn = QPushButton('Add', self)
        imagesAddBtn.setGeometry(750, 220, 80, 40)
        imagesAddBtn.setFont(QFont('Arial, 16'))

        #Datastores
        datastoresDataBtn = QPushButton('Data', self)
        datastoresDataBtn.setGeometry(400, 520, 80, 40)
        datastoresDataBtn.setFont(QFont('Arial, 16'))
        datastoresAddBtn = QPushButton('Add', self)
        datastoresAddBtn.setGeometry(500, 520, 80, 40)
        datastoresAddBtn.setFont(QFont('Arial, 16'))

if __name__ == '__main__':
    
    mainApp = QApplication(sys.argv)
    mv = mainWindow()
    
    sys.exit(mainApp.exec_())