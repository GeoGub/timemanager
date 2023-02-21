from PyQt6.QtCore import QTime, QTimer
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QTimeEdit, QVBoxLayout, QTextEdit

class TimeDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.time_edit = QTimeEdit(self)
        self.time_edit.setDisplayFormat('HH:mm:ss')

        self.text_edit = QTextEdit(self)

        self.button_box = QDialogButtonBox(
                QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, 
                self
            )
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addWidget(self.time_edit)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button_box)
        
        self.setWindowTitle("Выберите время")
        self.resize(200, 200)

    def get_time(self) -> QTime:
        return self.time_edit.time()
    
    def get_text(self) -> str:
        return self.text_edit.toPlainText()
