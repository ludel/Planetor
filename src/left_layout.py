from PySide2.QtWidgets import QVBoxLayout, QListWidget, QLineEdit, QCheckBox, QHBoxLayout, QComboBox


class LeftLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.list_corpus = QListWidget()

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Search ...')

        filter_layout = QHBoxLayout()
        self.is_planet = QCheckBox('Filter planet')
        filter_layout.addWidget(self.is_planet)

        self.order_box = QComboBox()
        self.order_box.addItems(['semi major Axis', 'aphelion', 'perihelion', 'gravity', 'density', 'sideral Orbit',
                                 'sideral Rotation', 'mass', 'volume'])
        self.order_box.setToolTip('Order by')
        filter_layout.addWidget(self.order_box)

        self.addWidget(self.line_edit)
        self.addLayout(filter_layout)
        self.addWidget(self.list_corpus)
