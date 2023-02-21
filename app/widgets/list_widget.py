import sys
from PyQt6.QtWidgets import (QLabel, QWidget, QHBoxLayout, QVBoxLayout, 
                             QListWidget, QListWidgetItem, QPushButton)
from PyQt6.QtCore import QTimer, Qt, QTime

class ListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.list_widget = QListWidget()

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.list_widget)

        self.setLayout(self.v_layout)

    def add_row(self, time: QTime, description):
        self.start_button = QPushButton("Start")
        self.time = time
        self.time_label = QLabel(self.time.toString("HH:mm:ss"))
        self.description = QLabel(description)
        self.button = QPushButton("Click")
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.start_button)
        h_layout.addWidget(self.time_label)
        h_layout.addWidget(self.description)
        h_layout.addWidget(self.button)

        self.start_button.clicked.connect(self.start_timer)
        self.button.clicked.connect(self.edit)

        widget = QWidget()
        widget.setLayout(h_layout)

        # Устанавливаем размер для элемента списка исходя из размера виджета
        item = QListWidgetItem()
        item.setSizeHint(widget.sizeHint())

        self.list_widget.addItem(item)

        # Добавляет виджет для отображения в элементе списка
        self.list_widget.setItemWidget(item, widget)

    def edit(self, *args):
        print(self.time_label.text(), self.description.text())

    def start_timer(self):
        self.timer.start(1000)

    def update(self):
        # self.time.setText(
        #         QTime(*map(int, self.time.text().split(":"))).addSecs(-1).toString("HH:mm:ss")
        #     )
        self.time.addSecs(-1)
        self.time_label.setText()
