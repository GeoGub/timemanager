from PyQt6.QtWidgets import QMainWindow, QApplication

import sys


class App(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setCentralWidget()


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    sys.exit(app.exec())