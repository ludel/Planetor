import pyqtgraph.opengl as gl
from PySide2.QtGui import QVector3D
from pyqtgraph import mkColor, Vector


class Graph(gl.GLViewWidget):
    def __init__(self):
        super().__init__()
        self.grid_size = 50
        self.pos_reduction = 1e-06

        self.default_vol = 0.01
        self.vol_sun = 20
        self.absolute_vol_sun = 1.412e18

        self.setCameraPosition(distance=self.grid_size, pos=Vector(0, 0, -10))
        """grid_vector = QVector3D(self.grid_size, self.grid_size, self.grid_size)

        x_grid = gl.GLGridItem(grid_vector, color=(255, 255, 255, 40))
        y_grid = gl.GLGridItem(grid_vector)
        z_grid = gl.GLGridItem(grid_vector)
        self.addItem(x_grid)
        self.addItem(y_grid)
        self.addItem(z_grid)"""

        sphere = gl.MeshData.sphere(15, 15, self.vol_sun)
        sun = gl.GLMeshItem(meshdata=sphere, color=mkColor(250, 250, 0))
        sun.translate(*self.get_position(1))

        self.addItem(sun)

    def get_vol(self, vol):
        return vol * 1e-11

    def get_position(self, position):
        return position / 1.5, position / 1.5, 1

    def build_perihelion(self, corpus):
        distance = corpus['semimajorAxis'] * self.pos_reduction
        if corpus['vol']:
            vol = self.get_vol(corpus['vol'])
        else:
            vol = self.default_vol

        sphere = gl.MeshData.sphere(15, 15, vol)
        sphere_item = gl.GLMeshItem(meshdata=sphere)
        sphere_item.translate(*self.get_position(distance))
        print(self.get_position(distance), distance, vol)
        self.addItem(sphere_item)
