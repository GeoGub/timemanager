from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QApplication, 
                             QDialog, QTimeEdit, QDialogButtonBox, QTableWidgetItem, 
                             QListWidget, QHBoxLayout, QLabel, QTableWidget)
from PyQt6.QtCore import QTime, QTimer

from dialogs.time_add import TimeDialog
from widgets.list_widget import ListWidget

class Main(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.button = QPushButton()
        self.table = QTableWidget()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        self.list = ListWidget()

        self.button.setText("Add new timer")
        self.button.clicked.connect(self._add_new_timer)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.list)

        self.setLayout(layout)

    def _add_new_timer(self):
        dialog = TimeDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.list.add_row(dialog.get_time(), dialog.get_text())


if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    widget.show()

    app.exec()
