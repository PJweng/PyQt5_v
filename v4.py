import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel('Username', self)
        self.pwd_label = QLabel('Password', self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())
