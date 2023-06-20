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
        self.lcdNumber.display(deger1)
        self.lcdNumber_2.display(deger2)
        self.lineEdit.setText(str(deger1 + deger2))
        self.sonuc_label.setText(str(deger1 + deger2))

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()

    def on_slider_change():
        deger1 = window.horizontalSlider.value()
        deger2 = window.dial.value()
        window.lcdNumber.display(deger1)
        window.lcdNumber_2.display(deger2)
        window.lineEdit.setText(str(deger1 + deger2))

    window.horizontalSlider.valueChanged.connect(on_slider_change)
    window.dial.valueChanged.connect(on_slider_change)

    window.show()
    app.exec()
