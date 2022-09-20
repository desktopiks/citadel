import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Window(QWidget):

    def __init__(self):
        super().__init__()

        screen_rect = QApplication.desktop().screenGeometry()
        screen_height, screen_width = screen_rect.height(), screen_rect.width()
        window_height, window_width = int(screen_height / 9) * 5, int(screen_width / 7) * 3  # move window size
        coordinate_window_height, coordinate_window_width = int(screen_height / 9) * 2, int(screen_width / 7) * 2 # move window coordinate
        self.move(coordinate_window_width, coordinate_window_height) # change window coordinate
        self.resize(window_width, window_height) # change window size
        self.show() # show window


def application():
    app = QApplication(sys.argv)
    game_window = Window()
    game_window.setWindowTitle('Citadels')
    sys.exit(app.exec_())


if __name__ == '__main__':
    # Creating apps and objects
    application()
