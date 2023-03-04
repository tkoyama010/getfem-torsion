import pyvista as pv
import numpy as np

mesh = pv.CylinderStructured(radius=np.linspace(1, 2, 5))
mesh.plot(show_edges=True)

pv.save_meshio("mesh.msh", mesh, file_format="gmsh", binary=False)

