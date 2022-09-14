from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow

import sys

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('Citadel')
    window.setGeometry(400, 250, 500, 300)

    main_text = QtWidgets.QLabel(window) #текст в центре
    main_text.setText('Citadel') #текст в центре
    main_text.move(225, 125) #текст в центре

    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    application()