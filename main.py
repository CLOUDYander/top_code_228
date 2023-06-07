import auto
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from db import *
from logic import *
import os


class ExapleApp(QtWidgets.QMainWindow, auto.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttom_ok.clicked.connect(self.auth)
        self.buttom_cancel.clicked.connect(self.cancel)

    def auth(self):
        login = self.login_input.text()
        password = self.pass_input.text()

        if user_authorization(login, password) == 1 and user_roles(login) == 'manager':
            self.close()
            os.system('python logic.py')
        else:
            self.close()

    def cancel(self):
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    Window = ExapleApp()
    Window.show()
    app.exec_()


if __name__ == "__main__":
    main()
