# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 600)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonOpen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOpen.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonOpen.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.gridLayout.addWidget(
            self.pushButtonOpen, 0, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.lineEditFile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFile.setEnabled(False)
        self.lineEditFile.setMinimumSize(QtCore.QSize(500, 30))
        self.lineEditFile.setObjectName("lineEditFile")
        self.gridLayout.addWidget(
            self.lineEditFile, 0, 1, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(
            self.label, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.lineEditTimes = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTimes.setEnabled(False)
        self.lineEditTimes.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEditTimes.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEditTimes.setObjectName("lineEditTimes")
        self.horizontalLayout_2.addWidget(
            self.lineEditTimes, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setMinimumSize(QtCore.QSize(200, 20))
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(
            self.checkBox, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setEnabled(False)
        self.pushButtonStart.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonStart.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.horizontalLayout.addWidget(
            self.pushButtonStart, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelPic = QtWidgets.QLabel(self.centralwidget)
        self.labelPic.setMinimumSize(QtCore.QSize(0, 80))
        self.labelPic.setText("")
        self.labelPic.setObjectName("labelPic")
        self.verticalLayout.addWidget(
            self.labelPic, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(
            self.label_2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.lineEditInput = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInput.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEditInput.sizePolicy().hasHeightForWidth())
        self.lineEditInput.setSizePolicy(sizePolicy)
        self.lineEditInput.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEditInput.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEditInput.setObjectName("lineEditInput")
        self.verticalLayout.addWidget(
            self.lineEditInput, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setMinimumSize(QtCore.QSize(94, 40))
        self.pushButtonBack.setMaximumSize(QtCore.QSize(94, 16777215))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.verticalLayout.addWidget(
            self.pushButtonBack, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(False)
        self.progressBar.setMinimumSize(QtCore.QSize(500, 40))
        self.progressBar.setSizeIncrement(QtCore.QSize(0, 0))
        self.progressBar.setBaseSize(QtCore.QSize(0, 0))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(
            self.progressBar, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.labelProgress = QtWidgets.QLabel(self.centralwidget)
        self.labelProgress.setMaximumSize(QtCore.QSize(200, 16777215))
        self.labelProgress.setText("")
        self.labelProgress.setObjectName("labelProgress")
        self.gridLayout_2.addWidget(
            self.labelProgress, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setEnabled(False)
        self.pushButtonSave.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonSave.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout_2.addWidget(
            self.pushButtonSave, 4, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.labelTimes = QtWidgets.QLabel(self.centralwidget)
        self.labelTimes.setMaximumSize(QtCore.QSize(200, 16777215))
        self.labelTimes.setText("")
        self.labelTimes.setObjectName("labelTimes")
        self.gridLayout_2.addWidget(
            self.labelTimes, 2, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(
            170, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.lineEditInput.returnPressed.connect(MainWindow.nextPic)
        self.pushButtonStart.clicked.connect(MainWindow.startLabel)
        self.pushButtonOpen.clicked.connect(MainWindow.openFile)
        self.pushButtonSave.clicked.connect(MainWindow.saveTemp)
        self.pushButtonBack.clicked.connect(MainWindow.backPic)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Captcha Label Tool"))
        self.pushButtonOpen.setText(_translate("MainWindow", "打开文件"))
        self.label.setText(_translate("MainWindow", "重复验证次数"))
        self.checkBox.setText(_translate("MainWindow", "是否完成上次未完成的标注"))
        self.pushButtonStart.setText(_translate("MainWindow", "开始标记"))
        self.label_2.setText(_translate("MainWindow", "完成输入后请按Enter切换到下一笔..."))
        self.pushButtonBack.setText(_translate("MainWindow", "回到上一笔"))
        self.pushButtonSave.setText(_translate("MainWindow", "暂时保存"))
