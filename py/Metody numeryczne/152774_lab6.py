# %% Zadanie 1 i 2

import numpy as np
from pso import PSO
import matplotlib.pyplot as plt


dims = 2
iters = 100

def f(x):
    x1,x2 = x
    return 0.26*(x1**2+x2**2)-0.48*x1*x2


alg = PSO(swarm_size=30,
phi_p=1,
phi_g=0.5,
omega=0.5,
v_max=2)



result = alg.run(f, [-10,10], dims, maximum_iterations=iters)

best_solution, global_best_particles, avg_fitness_values = result

print(f'x_min = {np.round(best_solution, 2)}')
print(f'f(x_min) = {f(best_solution):0.2f}')

x = np.arange(1,iters+1)

plt.plot(x,global_best_particles,label='Global best')
plt.plot(x,avg_fitness_values,label='Średnia wartość funkcji fitness')
plt.xlabel('ilość iteracji')
plt.legend()

plt.grid(True)

plt.show()

# %% Zadanie 3

dims = 1
iters = 100

def f2(x):
    return np.sin(10*np.pi*x)/2*x + (x-1)**4


alg = PSO(swarm_size=30,
phi_p=1,
phi_g=0.5,
omega=0.5,
v_max=2)


result = alg.run(f2, [0.5,2.5], dims, maximum_iterations=iters)
best_solution, global_best_particles, avg_fitness_values = result

print(f'x_min = {np.round(best_solution, 2)}')
print(f'f(x_min) = {f(best_solution):0.2f}')















# Raport
# Zaimplementowana funkcja to MATYAS function

# https://www.sfu.ca/~ssurjano/matya.html

# Granice: [-10,10]

# Ilość wymiarów: 2

# Testowane iteracje:
#  - 10
#  - 100


