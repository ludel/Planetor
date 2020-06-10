import json
import sys

from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel

from src.graph import Graph
from src.left_layout import LeftLayout
from src.right_layout import RightLayout

features_to_display = {
    'eccentricity': ('Eccentricity', ''), 'inclination': ('Inclination', '°'), 'density': ('Density', 'g.cm³'),
    'gravity': ('Gravity', 'm.s⁻²'), 'sideralOrbit': ('Sideral Orbit', 'Days'),
    'sideralRotation': ('Sideral Rotation', 'Hours'), 'discoveryDate': ('Discovery Date', ''),
    'discoveredBy': ('Discovered by', '')
}


class Widget(QWidget):
    def __init__(self, corpus):
        super().__init__()
        self.left = LeftLayout()
        self.right = RightLayout(len(features_to_display))

        self.corpus = corpus
        self.order_by('semimajorAxis')

        # Title
        self.vertical_layout = QVBoxLayout()
        self.title = QLabel()
        self.title.setFont(QFont('Times New Roman', 25, QFont.Bold))
        self.vertical_layout.addWidget(self.title)

        # Signals
        self.left.list_corpus.itemClicked.connect(self.change_corpus)
        self.left.line_edit.textChanged.connect(self.searching)
        self.left.is_planet.stateChanged.connect(self.filter_is_planet)
        self.left.order_box.currentTextChanged.connect(self.order_by)

        self.current_graph = Graph()
        self.right.addWidget(self.current_graph)

        # Main Layout
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addLayout(self.left)
        self.horizontal_layout.addLayout(self.right)

        # Select first QListWidgetItem
        self.left.list_corpus.setCurrentRow(0)
        first_widget_item = self.left.list_corpus.selectedItems()[0]
        self.change_corpus(first_widget_item)

        # Set the layout to the QWidget
        self.vertical_layout.addLayout(self.horizontal_layout)
        self.setLayout(self.vertical_layout)

    def change_corpus(self, current):
        current_corpus = self.corpus.get(current.text())
        self.title.setText(current.text())
        self.update_graph(current_corpus)

        for index, (feature, value) in enumerate(features_to_display.items()):
            feature_value = current_corpus[feature]
            if feature_value == 0:
                feature_value = '-'
            else:
                feature_value = f'{feature_value} {value[1]}'

            self.right.data_corpus.itemAt(index).widget().setText(f'{value[0]}: {feature_value}')

    def update_graph(self, current_corpus):
        self.current_graph.build_perihelion(current_corpus)

    def searching(self, text):
        self.left.is_planet.setChecked(False)

        for index in range(self.left.list_corpus.count()):
            corpus_names = self.left.list_corpus.item(index).text()
            hidden = not corpus_names.lower().startswith(text.lower())
            self.left.list_corpus.item(index).setHidden(hidden)

    def filter_is_planet(self):
        for index in range(self.left.list_corpus.count()):
            corpus_names = self.left.list_corpus.item(index).text()

            if self.left.is_planet.isChecked():
                hidden = not self.corpus[corpus_names]['isPlanet']
            else:
                hidden = False

            self.left.list_corpus.item(index).setHidden(hidden)

    def order_by(self, text):
        new_order = sorted([c for c in self.corpus.values()], key=lambda c: c[text.replace(' ', '')])
        self.left.list_corpus.clear()
        self.left.list_corpus.addItems(p['id'] for p in new_order)


class MainWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()
        self.setWindowTitle("Planetor")
        self.setCentralWidget(widget)


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    # QWidget
    with open('dataset/corpus.json', 'r') as file:
        all_corpus = json.loads(file.read())

    widget_corpus = Widget(all_corpus)

    # QMainWindow using QWidget as central widget
    window = MainWindow(widget_corpus)
    window.resize(800, 600)
    window.show()

    # Execute application
    sys.exit(app.exec_())
