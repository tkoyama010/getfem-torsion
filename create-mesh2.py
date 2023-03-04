import pyvista as pv
import numpy as np
import getfem as gf
from pyvista.examples import cells as example_cells, plot_cell

grid = pv.CylinderStructured(radius=np.linspace(0.0, 1.0, 2), theta_resolution=4, z_resolution=2)
block = pv.MultiBlock([grid]).combine(merge_points=True, tolerance=1.0e-15)
plotter = pv.Plotter((1, 2))
# plotter.add_mesh(grid, show_edges=True)
# plotter.show()
# example_cells.plot_cell(grid)
example_cells.plot_cell(grid, screenshot="before.png")
# example_cells.plot_cell(block, screenshot="after.png")

pv.save_meshio("mesh.msh", block, file_format="gmsh", binary=False)
# pv.save_meshio("mesh.msh", grid, file_format="gmsh", binary=False)
# pv.save_meshio("mesh.msh", pv.MultiBlock([grid]).combine(merge_points=True), file_format="gmsh", binary=False)

mesh = gf.Mesh("import", "gmsh", "mesh.msh")
print(mesh)

