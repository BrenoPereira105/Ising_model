# 2D_Ising_model
implementation of ising model

The ising model is a toy model for interactions in statistical mechanics. Here it is used the hamiltonian

H = -J \sum_{i,j} s_i s_j - \sum_{i}h_i s_i

It is also considered periodic boundary conditions, T^2 = R^2/Z^2. For simplification, it is considered that the system does not interact with external sources. Also, the boltzmann constant \kappa and the interaction energy J are considered to be \kappa = J = 1. Below is a 50x50 grid in its initial state

![alt text](https://github.com/BrenoPereira105/Ising_model/blob/main/10000000_steps_50_grid_t0.png)

and then after 10000000 interactions...

![alt text](https://github.com/BrenoPereira105/Ising_model/blob/main/10000000_steps_50_grid_tfinal.png)
