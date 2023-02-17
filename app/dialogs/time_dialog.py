from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QTimeEdit, QVBoxLayout


class TimeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.time_edit = QTimeEdit(self)
        self.time_edit.setDisplayFormat('HH:mm')
        self.time_edit.setTime(QTime.currentTime())

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addWidget(self.time_edit)
        layout.addWidget(self.button_box)
        
        self.setWindowTitle("Выберите время")
        self.resize(200, 200)

    def selected_time(self):
        return self.time_edit.time()
