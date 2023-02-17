from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QDialog, QTimeEdit, QDialogButtonBox, QListWidgetItem
from PyQt6.QtCore import QTime

from dialogs.time_dialog import TimeDialog
from widgets.list_widget import ListWidget

class Main(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.button = QPushButton()
        self.list_widget = ListWidget()
        self.button.setText("Add new timer")
        self.button.clicked.connect(self._add_new_timer)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)
        self.setStyleSheet("width: 100%;")

    def _add_new_timer(self):
        dialog = TimeDialog()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.list_widget.list.addItem(
                QListWidgetItem(dialog.selected_time().toString("HH:mm"))
            )



if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    widget.show()

    app.exec()
