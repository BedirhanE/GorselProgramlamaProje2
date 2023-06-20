from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from arayuz import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.toplama_islemi)

    def toplama_islemi(self):
        deger1 = self.horizontalSlider.value()
        deger2 = self.dial.value()
        toplam = deger1 + deger2
        self.lcdNumber.display(toplam)
        self.lcdNumber_2.display(toplam)
        self.lineEdit.setText(str(toplam))


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()

    def on_slider_change():
        deger1 = window.horizontalSlider.value()
        deger2 = window.dial.value()
        toplam = deger1 + deger2
        window.lcdNumber.display(toplam)
        window.lcdNumber_2.display(toplam)
        window.lineEdit.setText(str(toplam))

    window.horizontalSlider.valueChanged.connect(on_slider_change)
    window.dial.valueChanged.connect(on_slider_change)

    window.show()
    app.exec()
