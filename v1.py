import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton


if __name__ == '__main__':
    app = QApplication(sys.argv)
    btn = QPushButton("Button")
    btn.show()
    a = app.exec_()
    print(a)
    sys.exit(a)

