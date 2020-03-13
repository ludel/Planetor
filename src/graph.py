import pyqtgraph.opengl as gl
from PySide2.QtGui import QVector3D
from pyqtgraph import mkColor, Vector


class Graph(gl.GLViewWidget):
    def __init__(self, sun):
        super().__init__()
        self.setCameraPosition(distance=50, pos=Vector(0, 0, -10))
        grid_vector = QVector3D(50, 50, 50)

        self.dim_reduction_factor = 0.05
        self.distance_reduction_factor = 0.001

        x_grid = gl.GLGridItem(grid_vector, color=(255, 255, 255, 40))
        y_grid = gl.GLGridItem(grid_vector)
        z_grid = gl.GLGridItem(grid_vector)
        self.addItem(x_grid)
        self.addItem(y_grid)
        self.addItem(z_grid)

        sun_dim = int(sun['dimension'][:2]) * self.dim_reduction_factor
        target = gl.MeshData.sphere(15, 15, sun_dim)

        sun = gl.GLMeshItem(meshdata=target, color=mkColor(250, 250, 0))

        self.addItem(sun)

    def build_perihelion(self, perihelion):
        pass
