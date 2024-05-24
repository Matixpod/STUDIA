import numpy as np
from pso import PSO

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

print(f'x_min = {np.round(result, 2)}')
print(f'f(x_min) = {f(result):0.2f}')

# Raport
# Zaimplementowana funkcja to MATYAS function

# https://www.sfu.ca/~ssurjano/matya.html

# Granice: [-10,10]

# Ilość wymiarów: 2

# Testowane iteracje:
#  - 10
#  - 100


