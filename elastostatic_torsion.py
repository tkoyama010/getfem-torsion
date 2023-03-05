import getfem as gf

###############################################################################
# Numerical parameters

# Degree of the finite element methods
elements_degree = 1

###############################################################################
# Load mesh

mesh = gf.Mesh("load", "mesh.msh")

###############################################################################
# Boundary selection

fb1 = mesh.outer_faces_with_direction([0.0, 0.0, 1.0], 0.01)  # Top boundary
fb2 = mesh.outer_faces_with_direction([0.0, 0.0, -1.0], 0.01)  # Bottom boundary

TOP_BOUND = 1
BOTTOM_BOUND = 2

mesh.set_region(TOP_BOUND, fb1)
mesh.set_region(BOTTOM_BOUND, fb2)

###############################################################################
# Definition of finite elements methods and integration method

# Finite element for the elastic displacement
mfu = gf.MeshFem(mesh, 3)
mfu.set_classical_fem(elements_degree)

# Integration method
mim = gf.MeshIm(mesh, elements_degree * 2)
