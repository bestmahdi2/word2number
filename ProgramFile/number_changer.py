# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\number_changer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(559, 299)
        MainWindow.setMinimumSize(QtCore.QSize(559, 299))
        MainWindow.setMaximumSize(QtCore.QSize(559, 299))
        MainWindow.setWindowOpacity(0.978)
        MainWindow.setStyleSheet("color:#FCE400;background-color:#3C3F41;")
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 541, 31))
        self.lineEdit.setStyleSheet("background-color:#F5F5F5 ; color:black")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 5, 531, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("overflow : auto;")
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 140, 71, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setWhatsThis("")
        self.pushButton.setStyleSheet("background-color :#B8860B; color: black")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(230, 190, 91, 41))
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser.setStyleSheet("color:white ; align:\"center\";font-size:14px;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.textBrowser.setObjectName("textBrowser")
        self.label_Error = QtWidgets.QLabel(self.centralwidget)
        self.label_Error.setGeometry(QtCore.QRect(12, 104, 351, 16))
        self.label_Error.setStyleSheet("color:red;")
        self.label_Error.setText("")
        self.label_Error.setObjectName("label_Error")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 25, 531, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("overflow: auto;")
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(429, 101, 121, 20))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_P = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_P.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_P.setStyleSheet("color:#FF7F50")
        self.radioButton_P.setObjectName("radioButton_P")
        self.horizontalLayout.addWidget(self.radioButton_P)
        self.radioButton_E = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_E.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_E.setStyleSheet("color:#FF7F50")
        self.radioButton_E.setChecked(True)
        self.radioButton_E.setObjectName("radioButton_E")
        self.horizontalLayout.addWidget(self.radioButton_E)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 559, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Word2Number"))
        self.lineEdit.setStatusTip(_translate("MainWindow", "You can type here"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter your number here..."))
        self.label.setText(_translate("MainWindow", "Please enter your number in characters down below:"))
        self.pushButton.setToolTip(_translate("MainWindow", "Shortcut : Enter"))
        self.pushButton.setStatusTip(_translate("MainWindow", "Click to change number you entered"))
        self.pushButton.setText(_translate("MainWindow", "Change"))
        self.textBrowser.setStatusTip(_translate("MainWindow", "Reasults"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Remmber:\n"
"you need to enter at least one number before hundred , million and thousand , otherwise it\'s meaningless ."))
        self.radioButton_P.setToolTip(_translate("MainWindow", "Shortcut : CTRL + P"))
        self.radioButton_P.setStatusTip(_translate("MainWindow", "Change language"))
        self.radioButton_P.setText(_translate("MainWindow", "Persian"))
        self.radioButton_E.setToolTip(_translate("MainWindow", "Shortcut : CTRL + E"))
        self.radioButton_E.setStatusTip(_translate("MainWindow", "Change language"))
        self.radioButton_E.setText(_translate("MainWindow", "English"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
