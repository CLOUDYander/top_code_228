import design
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys
import mysql.connector
from mysql.connector import connect, Error
import main


try:
    with connect(
        host='192.168.15.95',
        port='3306',
        database='user48',
        user='user48',
        password='55907'
    ) as user48:
        mycursor = user48.cursor()

        class Graph(QtWidgets.QMainWindow, QApplication, QTableWidget, QTableWidgetItem, design.Ui_MainWindow):
            def __init__(self):
                super().__init__()
                self.setupUi(self)
                self.pushButton_5.clicked.connect(self.insert)
                self.pushButton_2.clicked.connect(self.resseting)
                self.pushButton_3.clicked.connect(self.delete)
                count = 0
                mycursor.execute(" SELECT * FROM Materials LIMIT 10")
                for i in mycursor:
                    self.tableWidget.insertRow(count)
                    self.tableWidget.setItem(
                        count, 0, QtWidgets.QTableWidgetItem(i[0]))
                    self.tableWidget.setItem(
                        count, 1, QtWidgets.QTableWidgetItem(i[1]))
                    self.tableWidget.setItem(
                        count, 2, QtWidgets.QTableWidgetItem(str(i[2])))
                    self.tableWidget.setItem(
                        count, 3, QtWidgets.QTableWidgetItem(str(i[3])))
                    self.tableWidget.setItem(
                        count, 4, QtWidgets.QTableWidgetItem(str(i[4])))
                    self.tableWidget.setItem(
                        count, 5, QtWidgets.QTableWidgetItem(str(i[5])))
                    self.tableWidget.setItem(
                        count, 6, QtWidgets.QTableWidgetItem(str(i[6])))
                    self.tableWidget.setItem(
                        count, 7, QtWidgets.QTableWidgetItem(str(i[7])))
                    self.tableWidget.setItem(
                        count, 8, QtWidgets.QTableWidgetItem(str(i[8])))
                    self.tableWidget.setItem(
                        count, 9, QtWidgets.QTableWidgetItem(str(i[9])))
                    count += 1

            def insert(self):
                chek = list(self.lineEdit.text())
                if chek[0].isdigit() == False:
                    sql = "INSERT INTO Materials (КодМатериала, ТипМатериала, Код_возможного_поставщика, Количество_в_упаковке, Единица_измерения, Количество_на_складе, Минимальное_допустимое_колличество, Описание, Изображение, Цена) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    val = (self.lineEdit.text(), self.comboBox.currentText(), self.comboBox_2.currentIndex(), self.spinBox.value(), self.comboBox_3.currentText(
                    ), self.spinBox_2.value(), self.spinBox_3.value(), self.plainTextEdit.toPlainText(), "-", self.spinBox_4.value())
                    mycursor.execute(sql, val)
                    user48.commit()
                    print(mycursor.rowcount, "record inserted.")
                    self.label_5.setText("Заполнение прошло успешно!")
                else:
                    self.label_5.setText(
                        "Название материала не может начинаться с чисел/цифры")

            def resseting(self):
                sql = "UPDATE Materials SET Наименование_материала =  %s, Тип_материала = %s, Код_возможного_поставщика = %s, Количество_в_упаковке = %s, Единица_измерения = %s, Количество_на_складе = %s, Минимальное_допустимое_колличество = %s, Описание = %s, Изображение = %s, Цена = %s WHERE Код_материала = " + \
                    str(self.tableWidget.selectionModel().selectedIndexes())
                val = (self.lineEdit.text(), self.comboBox.currentText(), self.comboBox_2.currentIndex(), self.spinBox.value(), self.comboBox_3.currentText(
                ), self.spinBox_2.value(), self.spinBox_3.value(), self.plainTextEdit.toPlainText(), "-", self.spinBox_4.value())
                mycursor.execute(sql, val)
                user48.commit()
                print(mycursor.rowcount, "record inserted.")

            def delete(self):
                print("Удалить")

        def main():
            app = QtWidgets.QApplication(sys.argv)
            Window = Graph()
            Window.show()
            app.exec_()
        if __name__ == "__main__":
            main()

except Error as er:
    class dbError(QtWidgets.QMainWindow, QApplication, QTableWidget, QTableWidgetItem, design.Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.label_5.setText("Ошибка подключения к бд")

    def main():
        app = QtWidgets.QApplication(sys.argv)
        Window = dbError()
        Window.show()
        app.exec_()
    if __name__ == "__main__":
        main()
    print(er)
