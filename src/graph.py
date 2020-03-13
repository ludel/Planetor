import pyqtgraph.opengl as gl
from PySide2.QtGui import QVector3D


class Graph:
    def __init__(self):
        super().__init__()
        self.widget = None

    def build_perihelion(self, perihelion):
        del self.widget
        self.widget = gl.GLViewWidget()
        grid_vector = QVector3D(50, 50, 50)
        x_grid = gl.GLGridItem(grid_vector)
        y_grid = gl.GLGridItem(grid_vector)
        z_grid = gl.GLGridItem(grid_vector)
        sun = gl.GLBoxItem()
        sun.setSize(1, 1, 1)

        self.widget.addItem(x_grid)
        self.widget.addItem(y_grid)
        self.widget.addItem(z_grid)
        self.widget.addItem(sun)
