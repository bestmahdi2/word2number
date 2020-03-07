from PyQt5 import QtWidgets, QtCore
from ProgramFile.number_changer import Ui_MainWindow
from ProgramFile.compiler1P import mainsP
from ProgramFile.compiler1 import mains

# Hidpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
# use Hidpi icons
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Ui(Ui_MainWindow):
    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))
        self.radioButton_E.setShortcut(_translate("MainWindow", "CTRL+E"))
        self.radioButton_P.setShortcut(_translate("MainWindow", "CTRL+P"))

    def wrong_entrance(self):
        self.label_Error.setText("Wrong entrance")
        ui.label_Error.setStyleSheet("color:red;")

    def pushB_clicked(self):
        text = self.lineEdit.text().lower()
        check = self.radioButton_E.isChecked()
    ##just for fun :
        textlist = text.split(" ")
        if "hello" in textlist or "hi" in textlist:
            self.textBrowser.setText("Hello!")
        if "master" in textlist or "mysterious" in textlist or "programmer" in textlist or "maker" in textlist or "mahdi" in textlist:
            self.textBrowser.setText("That is me!")
        if "fuck" in textlist or "fucking" in textlist or "bitch" in textlist or "shit" in textlist or "asshole" in textlist or "damn" in textlist or "cock" in textlist or "penis" in textlist or "pussy" in textlist or "vagina" in textlist or "cunt" in textlist:
            self.textBrowser.setText("Fuck off!")
    ##just for fun .
        elif check == True:
            try:
                m = mains(text)
                m.results()
                self.textBrowser.setText(str(m.num))
                if m.dup == "yes":
                    ui.label_Error.setText("Wrong format because of repeated entrance but it still has its own answer")
                    ui.label_Error.setStyleSheet("color:green;")
            except:
                self.wrong_entrance()

        elif check == False:
            try:
                m = mainsP(text)
                m.results()
                self.textBrowser.setText(str(m.num))
                if m.dup == "yes":
                    ui.label_Error.setText("Wrong format because of repeated entrance but it still has its own answer")
                    ui.label_Error.setStyleSheet("color:green;")
            except:
                self.wrong_entrance()

    def enter_language(self):
        english = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z", " ","-"]
        persian = ["ا", "آ", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض", "ط",
                   "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "ن", "و", "ه", "ی", "م", " "]

        check = ui.radioButton_E.isChecked()
        text = ui.lineEdit.text().lower()

        if check == True:
            for i in text:
                if i not in english:
                    ui.label_Error.setStyleSheet("color:#3AE2CE;")
                    ui.label_Error.setText("Wrong language selected")
                    ui.pushButton.setEnabled(False)
                else:
                    ui.label_Error.setText("")
                    ui.pushButton.setEnabled(True)
            # for i in textlist:
            #     if i not in numbers_E:
            #         ui.label_Error.setText("wrong enterence")
            #         ui.pushButton.setEnabled(False)
            #     else:
            #         ui.label_Error.setText("")
            #         ui.pushButton.setEnabled(True)
        if check == False:
            for i in text:
                if i not in persian:
                    ui.label_Error.setStyleSheet("color:#3AE2CE;")
                    ui.label_Error.setText("Wrong language selected")
                    ui.pushButton.setEnabled(False)
                else:
                    ui.label_Error.setText("")
                    ui.pushButton.setEnabled(True)
            # for i in textlist:
            #     if i not in numbers_P:
            #         ui.label_Error.setText("wrong enterence")
            #         ui.pushButton.setEnabled(False)
            #     else:
            #         ui.label_Error.setText("")
            #         ui.pushButton.setEnabled(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui()
    ui.setupUi(MainWindow)
    ###

    ui.radioButton_E.setChecked(True)


    ui.pushButton.clicked.connect(ui.pushB_clicked)
    ui.lineEdit.textEdited.connect(ui.enter_language)
    ui.radioButton_E.clicked.connect(ui.enter_language)
    ui.radioButton_P.clicked.connect(ui.enter_language)
    ###
    MainWindow.show()
    sys.exit(app.exec_())
