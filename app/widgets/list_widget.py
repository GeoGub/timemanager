from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QVBoxLayout

class ListWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.list = QListWidget()
        # self.list.addItem(QListWidgetItem("Item 1"))
        # self.list.addItem(QListWidgetItem("Item 2"))
        # self.list.addItem(QListWidgetItem("Item 3"))
        layout = QVBoxLayout()
        layout.addWidget(self.list)

        self.setLayout(layout)


