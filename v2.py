import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.label = QLabel('Lable', self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())
