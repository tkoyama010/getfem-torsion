import getfem as gf
import numpy as np
import pyvista as pv

###############################################################################

d = 100.0  # mm
L = 500.0  # mm

###############################################################################

mesh = gf.Mesh("empty", 3)

mesh.add_convex(
    gf.GeoTrans("GT_PRISM(3,1)"),
    [
        [
            0,
            d / 16 * np.cos(0.0),
            d / 16 * np.cos(np.pi / 8),
            0,
            d / 16 * np.cos(0.0),
            d / 16 * np.cos(np.pi / 8),
        ],
        [
            0,
            d / 16 * np.sin(0.0),
            d / 16 * np.sin(np.pi / 8),
            0,
            d / 16 * np.sin(0.0),
            d / 16 * np.sin(np.pi / 8),
        ],
        [0, 0, 0, L / 25, L / 25, L / 25],
    ],
)

mesh.export_to_vtk("mesh.vtk", "ascii")

m = pv.read("mesh.vtk")
m.plot(cpos="xy", show_edges=True)
