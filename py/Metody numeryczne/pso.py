import copy
import numpy as np

class PSO:
    class Particle:
        def __init__(self, f, domain, dims, v_max):
            a, b = domain
            self.x = np.random.rand(dims)
            self.x = (b-a) * self.x + a

            self.x_best = self.x.copy()

            a, b = -v_max/3, v_max/3
            self.v = (b-a) * np.random.rand(dims) + a

            self.f_value = f(self.x)
            self.f_best_value = f(self.x_best)


    def __init__(self, swarm_size, phi_p, phi_g, omega, v_max):
        self.N = swarm_size
        self.phi_p = phi_p
        self.phi_g = phi_g
        self.omega = omega
        self.v_max = v_max

    def run(self, ff, domain, dims, maximum_iterations=10):
        self.gb = []
        self.avg_ff = []
        
        swarm = [PSO.Particle(ff, domain, dims, self.v_max)
                 for i in range(self.N)]

        global_best = copy.deepcopy(min(swarm, key=lambda p: p.f_value))

        for i in range(maximum_iterations):
            for part in swarm:
                if part.f_value < part.f_best_value:
                    part.x_best = part.x.copy()
                    part.f_best_value = ff(part.x_best)

                if part.f_best_value < global_best.f_value:
                    global_best = copy.deepcopy(part)

            self.gb.append(global_best.f_value)  

            
            avg_fitness = np.mean([part.f_value for part in swarm])
            self.avg_ff.append(avg_fitness)

            for part in swarm:
                part.v = self.omega * part.v\
                          + self.phi_p * np.random.rand()\
                          * (part.x_best - part.x\
                             + self.phi_g * np.random.rand())\
                          * (global_best.x - part.x)

                part.x = part.x + part.v
                part.x[part.x < domain[0]] = domain[0]
                part.x[part.x > domain[1]] = domain[1]
                part.f_value = ff(part.x)
                part.v[part.v > self.v_max] = self.v_max

        return min(swarm, key=lambda p: p.f_value).x, self.gb, self.avg_ff
