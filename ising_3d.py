import numpy as np
import sys
import matplotlib.pyplot as plt
import math
from matplotlib import animation

def corrector(a, size_num):

    if a < 0:
       a = size_num + a

    return a

def flip_condition(A, s_x, s_y, s_z, steps, size):

    flip = 0

    energy_before = A[s_x][s_y][s_z] + \
                    A[(s_x + 1)%(size_num-1)][s_y][s_z] + \
                    A[corrector(s_x - 1, size_num)][s_y][s_z] + \
                    A[s_x][(s_y + 1)%(size_num-1)][s_z] + \
                    A[s_x][corrector(s_y - 1, size_num)][s_z] + \
                    A[s_x][s_y][(s_z + 1)%(size_num-1)] + \
                    A[s_x][s_y][corrector(s_z - 1, size_num)]
    
    b = A[s_x][s_y][s_z]
    b = (b+1)%2
    
    energy_after =  b + \
                    A[(s_x + 1)%(size_num-1)][s_y][s_z] + \
                    A[corrector(s_x - 1, size_num)][s_y][s_z] + \
                    A[s_x][(s_y + 1)%(size_num-1)][s_z] + \
                    A[s_x][corrector(s_y - 1, size_num)][s_z] + \
                    A[s_x][s_y][(s_z + 1)%(size_num-1)] + \
                    A[s_x][s_y][corrector(s_z - 1, size_num)]
 
    delta_energy = energy_after - energy_before

    r = np.random.randint(2)
    
    if r < math.exp(-delta_energy/(steps)):
           flip = 1
   
    return flip
    
size_num = int(sys.argv[2])
A = np.random.randint(2, size=(size_num, size_num, size_num))

for i in range(size_num):
    for j in range(size_num):
        for k in range(size_num):
            if A[i][j][k] == 0:
                A[i][j][k] = -1

steps = int(sys.argv[1])
print("steps: ", steps)

print("size: ", size_num)

x = np.arange(A.shape[0])[:, None, None]
y = np.arange(A.shape[1])[None, :, None]
z = np.arange(A.shape[2])[None, None, :]
x, y, z = np.broadcast_arrays(x, y, z)


c_color = np.tile(A.ravel()[:, None], [1, 3])

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(x.ravel(),
           y.ravel(),
           z.ravel(),
           c=A)

plt.show()

for t in range(steps):

           s_x = np.random.randint(size_num)
           s_y = np.random.randint(size_num)
           s_z = np.random.randint(size_num)   
           
           if flip_condition(A, s_x, s_y, s_z, steps, size_num) == 1:
              if A[s_x][s_y][s_z] == 1:
                 A[s_x][s_y][s_z] = -1
              else:
                 A[s_x][s_y][s_z] = 1
           print("time: ", t)
          
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(x.ravel(),
           y.ravel(),
           z.ravel(),
           c=A)

plt.show()
