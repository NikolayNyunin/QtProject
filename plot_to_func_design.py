# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_to_func_design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 710)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plotWidget = PlotWidget(self.centralwidget)
        self.plotWidget.setGeometry(QtCore.QRect(40, 80, 521, 251))
        self.plotWidget.setObjectName("plotWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 350, 521, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_5 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 2, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout.addWidget(self.radioButton_6, 2, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setCheckable(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 0, 1, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 1, 1, 1, 1)
        self.funcEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.funcEdit.setGeometry(QtCore.QRect(150, 640, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.funcEdit.setFont(font)
        self.funcEdit.setText("")
        self.funcEdit.setObjectName("funcEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 10, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.white = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.white.setFont(font)
        self.white.setMouseTracking(True)
        self.white.setChecked(True)
        self.white.setObjectName("white")
        self.horizontalLayout.addWidget(self.white)
        self.red = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.red.setFont(font)
        self.red.setObjectName("red")
        self.horizontalLayout.addWidget(self.red)
        self.green = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.green.setFont(font)
        self.green.setObjectName("green")
        self.horizontalLayout.addWidget(self.green)
        self.blue = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.blue.setFont(font)
        self.blue.setObjectName("blue")
        self.horizontalLayout.addWidget(self.blue)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 105, 49))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(210, 500, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delButton.setFont(font)
        self.delButton.setObjectName("delButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 650, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.coordsEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.coordsEdit.setGeometry(QtCore.QRect(270, 570, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.coordsEdit.setFont(font)
        self.coordsEdit.setText("")
        self.coordsEdit.setObjectName("coordsEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 580, 221, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_5.setText(_translate("MainWindow", "Кубическая функция"))
        self.radioButton_2.setText(_translate("MainWindow", "Корневая функция"))
        self.radioButton_6.setText(_translate("MainWindow", "Синус"))
        self.radioButton.setText(_translate("MainWindow", "Прямая (по двум точкам)"))
        self.radioButton_4.setText(_translate("MainWindow", "Квадратичная функция"))
        self.radioButton_3.setText(_translate("MainWindow", "Модульная функция"))
        self.white.setText(_translate("MainWindow", "Белый"))
        self.red.setText(_translate("MainWindow", "Красный"))
        self.green.setText(_translate("MainWindow", "Зелёный"))
        self.blue.setText(_translate("MainWindow", "Синий"))
        self.label.setText(_translate("MainWindow", "Цвет графика:"))
        self.delButton.setText(_translate("MainWindow", "Очистить"))
        self.label_3.setText(_translate("MainWindow", "Функция:"))
        self.label_2.setText(_translate("MainWindow", "Текущие координаты:"))

from pyqtgraph import PlotWidget