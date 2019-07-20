import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.label = QLabel('Lable', self)
        self.btn = QPushButton('Button', self)

        self.label.move(20, 0)
        self.btn.move(50, 50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())
