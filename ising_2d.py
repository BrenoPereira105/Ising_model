import numpy as np
import sys
import matplotlib.pyplot as plt
import math
from matplotlib import animation

def corrector(a, size_num):

    if a < 0:
       a = size_num + a

    return a

def flip_condition(A, s_x, s_y, steps, size):

    flip = 0

    energy_before = A[s_x][s_y] + \
                    A[(s_x + 1)%(size_num-1)][s_y] + \
                    A[corrector(s_x - 1, size_num)][s_y] + \
                    A[s_x][(s_y + 1)%(size_num-1)] + \
                    A[s_x][corrector(s_y - 1, size_num)]
    b = A[s_x][s_y]
    b = (b+1)%2
    
    energy_after =  b + \
                    A[(s_x + 1)%(size_num-1)][s_y] + \
                    A[corrector(s_x - 1, size_num)][s_y] + \
                    A[s_x][(s_x + 1)%(size_num-1)] + \
                    A[s_x][corrector(s_y - 1, size_num)] 

    delta_energy = energy_after - energy_before

    r = np.random.randint(2)
    
    if r < math.exp(-delta_energy/(steps)):
           flip = 1
   
    return flip
    
size_num = int(sys.argv[2])
A = np.random.randint(2, size=(size_num,size_num))

for i in range(size_num):
    for j in range(size_num):
        if A[i][j] == 0:
             A[i][j] = -1

steps = int(sys.argv[1])
print("steps: ", steps)


print("size: ", size_num)

plt.imshow(A)
plt.show()

for t in range(steps):

           s_x = np.random.randint(size_num)
           s_y = np.random.randint(size_num)  
           
           if flip_condition(A, s_x, s_y, steps, size_num) == 1:
              if A[s_x][s_y] == 1:
                 A[s_x][s_y] = -1
              else:
                 A[s_x][s_y] = 1
           print("time: ", t)
          
plt.imshow(A)
plt.show()
