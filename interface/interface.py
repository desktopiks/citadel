import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()  #Drawing the interface to method InitUi

    def initUI(self):
        self.desktop = QApplication.desktop()

        #Get the screen sizes 
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()

        #Show the window
        self.show()


def Application():
    app = QApplication(sys.argv)
    ex = Example()
    ex.setWindowTitle('Citadels')
    sys.exit(app.exec_())


if __name__ == '__main__':
    #Creating apps and objects
    Application()
