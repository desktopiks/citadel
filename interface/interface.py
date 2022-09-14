from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow

import sys

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('Citadel')
    window.setGeometry(400, 250, 500, 300)

    main_text = QtWidgets.QLabel(window) #text in the center
    main_text.setText('Citadel') #text in the center
    main_text.move(225, 125) #text in the center

    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    application()