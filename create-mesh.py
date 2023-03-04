import getfem as gf
import numpy as np
import pyvista as pv

###############################################################################

d = 100.0  # mm
L = 500.0  # mm

###############################################################################

mesh = gf.Mesh("empty", 3)

rhos = np.linspace(0.0, d / 2, 8 + 1)
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
        for k, rho in enumerate(rhos[1:]):
            mesh.add_convex(
                gf.GeoTrans("GT_QK(3,1)"),
                [
                    [
                        rhos[k] * np.cos(phis[j]),
                        rhos[k] * np.cos(phi),
                        rho * np.cos(phis[j]),
                        rho * np.cos(phi),
                        rhos[k] * np.cos(phis[j]),
                        rhos[k] * np.cos(phi),
                        rho * np.cos(phis[j]),
                        rho * np.cos(phi),
                    ],
                    [
                        rhos[k] * np.sin(phis[j]),
                        rhos[k] * np.sin(phi),
                        rho * np.sin(phis[j]),
                        rho * np.sin(phi),
                        rhos[k] * np.sin(phis[j]),
                        rhos[k] * np.sin(phi),
                        rho * np.sin(phis[j]),
                        rho * np.sin(phi),
                    ],
                    [zs[i], zs[i], zs[i], zs[i], z, z, z, z],
                ],
            )

mesh.export_to_vtk("mesh.vtk", "ascii")

m = pv.read("mesh.vtk")
m.plot(cpos="xy", show_edges=True)
