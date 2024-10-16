# %%
import numpy as np
from pso import PSO
import matplotlib.pyplot as plt
# %% Matyas Function
def matyas_function(x):
    x1, x2 = x
    return 0.26 * (x1**2 + x2**2) - 0.48 * x1 * x2

dims = 2
iters = 100

alg = PSO(swarm_size=30, phi_p=1, phi_g=0.5, omega=0.5, v_max=2)

result = alg.run(matyas_function, [-10, 10], dims, maximum_iterations=iters)

best_solution, global_best_particles, avg_fitness_values = result

print(f'x_min = {np.round(best_solution, 2)}')
print(f'f(x_min) = {matyas_function(best_solution):0.2f}')

x = np.arange(1, iters + 1)

plt.plot(x, global_best_particles, label='Global best')
plt.plot(x, avg_fitness_values, label='Średnia wartość funkcji fitness')
plt.xlabel('ilość iteracji')
plt.legend()

plt.grid(True)

plt.show()

# %% Booth Function
def booth_function(x):
    x1, x2 = x
    return (x1 + 2 * x2 - 7)**2 + (2 * x1 + x2 - 5)**2

dims = 2
iters = 100

alg = PSO(swarm_size=30, phi_p=1, phi_g=0.5, omega=0.5, v_max=2)

result = alg.run(booth_function, [-10, 10], dims, maximum_iterations=iters)

best_solution, global_best_particles, avg_fitness_values = result

print(f'x_min = {np.round(best_solution, 2)}')
print(f'f(x_min) = {booth_function(best_solution):0.2f}')

x = np.arange(1, iters + 1)

plt.plot(x, global_best_particles, label='Global best')
plt.plot(x, avg_fitness_values, label='Średnia wartość funkcji fitness')
plt.xlabel('ilość iteracji')
plt.legend()

plt.grid(True)

plt.show()

# %% Schaffer Function N. 2

def schaffer_function_n2(x):
    x1, x2 = x
    numerator = np.sin(x1**2 - x2**2)**2 - 0.5
    denominator = (1 + 0.001 * (x1**2 + x2**2))**2
    return 0.5 + numerator / denominator

dims = 2
iters = 1000

alg = PSO(swarm_size=30, phi_p=1, phi_g=1, omega=0.5, v_max=2)

result = alg.run(schaffer_function_n2, [-10, 10], dims, maximum_iterations=iters)

best_solution, global_best_particles, avg_fitness_values = result

print(f'x_min = {np.round(best_solution, 2)}')
print(f'f(x_min) = {schaffer_function_n2(best_solution):0.2f}')

x = np.arange(1, iters + 1)
plt.plot(x, global_best_particles, label='Global best')
plt.plot(x, avg_fitness_values, label='Średnia wartość funkcji fitness')
plt.xlabel('Ilość iteracji')
plt.legend()
plt.grid(True)
plt.show()

# %% Levy Function N. 13

def levy_function_n13(x):
    x1, x2 = x
    return (np.sin(3 * np.pi * x1)**2
            + (x1 - 1)**2 * (1 + np.sin(3 * np.pi * x2)**2)
            + (x2 - 1)**2 * (1 + np.sin(2 * np.pi * x2)**2))

dims = 2
iters = 100

alg = PSO(swarm_size=30, phi_p=1, phi_g=1, omega=0.5, v_max=2)

result = alg.run(levy_function_n13, [-10, 10], dims, maximum_iterations=iters)

best_solution, global_best_particles, avg_fitness_values = result

print(f'x_min = {np.round(best_solution, 2)}')
print(f'f(x_min) = {levy_function_n13(best_solution):0.2f}')

x = np.arange(1, iters + 1)
plt.plot(x, global_best_particles, label='Global best')
plt.plot(x, avg_fitness_values, label='Średnia wartość funkcji fitness')
plt.xlabel('Ilość iteracji')
plt.legend()
plt.grid(True)
plt.show()


# Raport
# Zaimplementowana funkcja to MATYAS function

# https://www.sfu.ca/~ssurjano/matya.html

# Granice: [-10,10]

# Ilość wymiarów: 2

# Testowane iteracje:
#  - 10
#  - 100


