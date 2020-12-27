# Ising_model
implementation of ising model with monte carlo method

The ising model is a toy model for interactions in statistical mechanics. Here it is used the hamiltonian

H = -J \sum_{i,j} s_i s_j - \sum_{i}h_i s_i

It is also considered periodic boundary conditions, T^2 = R^2/Z^2. For simplification, it is considered that the system does not interact with external sources (h_i = 0). Also, the boltzmann constant \kappa and the interaction energy J are considered to be \kappa = J = 1. Below is a 50x50 grid in its initial random state

![alt text](https://github.com/BrenoPereira105/Ising_model/blob/main/10000000_steps_50_grid_t0.png)

and then after 10000000 interactions...

![alt text](https://github.com/BrenoPereira105/Ising_model/blob/main/10000000_steps_50_grid_tfinal.png)

Below is a 1000x1000 grid in its initial random state

![alt text](https://github.com/BrenoPereira105/Ising_model/blob/main/1000000_steps_1000_grid_t0.png)

and then after 1000000 interactions...

![alt text](https://github.com/BrenoPereira105/Ising_model/blob/main/1000000_steps_1000_grid_tfinal.png)

I also generated a 3d grid. Below is a 15x15x15 cube in its initial random state

![alt text](https://github.com/BrenoPereira105/Ising_model/blob/main/100000_steps_15_grid_t0.png)

and then after 100000 interactions...

![alt text](https://github.com/BrenoPereira105/Ising_model/blob/main/100000_steps_15_grid_tfinal.png)

