from PySide2.QtCore import Qt
from PySide2.QtWidgets import QVBoxLayout, QLabel, QGridLayout


class RightLayout(QVBoxLayout):
    def __init__(self, feature_count):
        super().__init__()

        # Table widget
        self.data_corpus = QGridLayout()
        self.data_corpus.setAlignment(Qt.AlignCenter)

        for _ in range(feature_count):
            label = QLabel()
            label.setStyleSheet('background-color: white; padding:2;')
            label.setMaximumWidth(350)
            self.data_corpus.addWidget(label)

        self.addLayout(self.data_corpus)
