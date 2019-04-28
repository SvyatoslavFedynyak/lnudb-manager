# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uis/dataInfo.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dataInfo(object):
    def setupUi(self, dataInfo):
        dataInfo.setObjectName("dataInfo")
        dataInfo.resize(800, 600)
        self.itemName = QtWidgets.QLabel(dataInfo)
        self.itemName.setGeometry(QtCore.QRect(110, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.itemName.setFont(font)
        self.itemName.setObjectName("itemName")
        self.editButton = QtWidgets.QPushButton(dataInfo)
        self.editButton.setGeometry(QtCore.QRect(340, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.editButton.setFont(font)
        self.editButton.setObjectName("editButton")
        self.removeButton = QtWidgets.QPushButton(dataInfo)
        self.removeButton.setGeometry(QtCore.QRect(570, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.removeButton.setFont(font)
        self.removeButton.setObjectName("removeButton")
        self.dataTable = QtWidgets.QTableWidget(dataInfo)
        self.dataTable.setGeometry(QtCore.QRect(30, 100, 731, 471))
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setColumnCount(0)
        self.dataTable.setRowCount(0)

        self.retranslateUi(dataInfo)
        QtCore.QMetaObject.connectSlotsByName(dataInfo)

    def retranslateUi(self, dataInfo):
        _translate = QtCore.QCoreApplication.translate
        dataInfo.setWindowTitle(_translate("dataInfo", "Data Info"))
        self.itemName.setText(_translate("dataInfo", "Name"))
        self.editButton.setText(_translate("dataInfo", "Edit"))
        self.removeButton.setText(_translate("dataInfo", "Remove "))


