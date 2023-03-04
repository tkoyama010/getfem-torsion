import getfem as gf
import numpy as np
import pyvista as pv

###############################################################################

d = 100.0  # mm
L = 500.0  # mm

###############################################################################

mesh = gf.Mesh("empty", 3)

heights = np.linspace(0.0, L, 25 + 1)

for i, height in enumerate(heights[1:]):
    mesh.add_convex(
        gf.GeoTrans("GT_PRISM(3,1)"),
        [
            [
                0,
                d / 16 * np.cos(np.pi / 8 * 0),
                d / 16 * np.cos(np.pi / 8 * 1),
                0,
                d / 16 * np.cos(np.pi / 8 * 0),
                d / 16 * np.cos(np.pi / 8 * 1),
            ],
            [
                0,
                d / 16 * np.sin(np.pi / 8 * 0),
                d / 16 * np.sin(np.pi / 8 * 1),
                0,
                d / 16 * np.sin(np.pi / 8 * 0),
                d / 16 * np.sin(np.pi / 8 * 1),
            ],
            [heights[i], heights[i], heights[i], height, height, height],
        ],
    )
    mesh.add_convex(
        gf.GeoTrans("GT_PRISM(3,1)"),
        [
            [
                0,
                d / 16 * np.cos(np.pi / 8 * 1),
                d / 16 * np.cos(np.pi / 8 * 2),
                0,
                d / 16 * np.cos(np.pi / 8 * 1),
                d / 16 * np.cos(np.pi / 8 * 2),
            ],
            [
                0,
                d / 16 * np.sin(np.pi / 8 * 1),
                d / 16 * np.sin(np.pi / 8 * 2),
                0,
                d / 16 * np.sin(np.pi / 8 * 1),
                d / 16 * np.sin(np.pi / 8 * 2),
            ],
            [heights[i], heights[i], heights[i], height, height, height],
        ],
    )

mesh.export_to_vtk("mesh.vtk", "ascii")

m = pv.read("mesh.vtk")
m.plot(cpos="xy", show_edges=True)
