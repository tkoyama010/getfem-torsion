import getfem as gf
import numpy as np
import pyvista as pv

mesh = gf.Mesh("empty", 3)

mesh.add_convex(
    gf.GeoTrans("GT_PRISM(3,1)"),
    [[0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 1, 1]],
)

mesh.export_to_vtk("mesh.vtk", "ascii")

m = pv.read("mesh.vtk")
m.plot(cpos="xy")

