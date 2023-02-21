from PyQt6.QtWidgets import QFrame, QHBoxLayout, QWidget, QTabWidget, QApplication, QVBoxLayout
from PyQt6.QtGui import QScreen

from datetime import datetime, timedelta

class Header(QWidget):
    def __init__(self) -> None:
        super().__init__()

        three_days_ago = datetime.now().date() - timedelta(days=3)

        self.tab = QTabWidget()

        # times = "--------".join([i for i in range(24)])

        for i in range(7):
            tab = QFrame()
            vertical_layout = QVBoxLayout()
            tab.setLayout(vertical_layout)
            date = three_days_ago+timedelta(days=i)
            self.tab.addTab(tab, date.strftime("%a, %m, %d"))

        layout = QHBoxLayout()
        layout.addWidget(self.tab)

        self.tab.setCurrentIndex(3)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    widget = Header()
    widget.show()

    app.exec()