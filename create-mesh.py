import getfem as gf
import numpy as np
import pyvista as pv

###############################################################################

d = 100.0  # mm
L = 500.0  # mm

###############################################################################

mesh = gf.Mesh("empty", 3)

phis = np.linspace(0.0, 2.0 * np.pi, 16 + 1)
zs = np.linspace(0.0, L, 25 + 1)

for i, z in enumerate(zs[1:]):
    for j, phi in enumerate(phis[1:]):
        mesh.add_convex(
            gf.GeoTrans("GT_PRISM(3,1)"),
            [
                [
                    0,
                    d / 16 * 1 * np.cos(phis[j]),
                    d / 16 * 1 * np.cos(phi),
                    0,
                    d / 16 * 1 * np.cos(phis[j]),
                    d / 16 * 1 * np.cos(phi),
                ],
                [
                    0,
                    d / 16 * 1 * np.sin(phis[j]),
                    d / 16 * 1 * np.sin(phi),
                    0,
                    d / 16 * 1 * np.sin(phis[j]),
                    d / 16 * 1 * np.sin(phi),
                ],
                [zs[i], zs[i], zs[i], z, z, z],
            ],
        )
        mesh.add_convex(
            gf.GeoTrans("GT_QK(3,1)"),
            [
                [
                    d / 16 * 1 * np.cos(phis[j]),
                    d / 16 * 1 * np.cos(phi),
                    d / 16 * 2 * np.cos(phis[j]),
                    d / 16 * 2 * np.cos(phi),
                    d / 16 * 1 * np.cos(phis[j]),
                    d / 16 * 1 * np.cos(phi),
                    d / 16 * 2 * np.cos(phis[j]),
                    d / 16 * 2 * np.cos(phi),
                ],
                [
                    d / 16 * 1 * np.sin(phis[j]),
                    d / 16 * 1 * np.sin(phi),
                    d / 16 * 2 * np.sin(phis[j]),
                    d / 16 * 2 * np.sin(phi),
                    d / 16 * 1 * np.sin(phis[j]),
                    d / 16 * 1 * np.sin(phi),
                    d / 16 * 2 * np.sin(phis[j]),
                    d / 16 * 2 * np.sin(phi),
                ],
                [zs[i], zs[i], zs[i], zs[i], z, z, z, z],
            ],
        )

mesh.export_to_vtk("mesh.vtk", "ascii")

m = pv.read("mesh.vtk")
m.plot(cpos="xy", show_edges=True)
