import numpy as np

import matplotlib.pyplot as plt


# sn = 90
# sr = 55

# a = 300
# b = 300
# c = 400


# 0.1*n + 0.2*r <= 300
# 0.3*n + 0.1*r <= 300
# 0.5*n + 0*r <= 400




n = np.arange(0, 1001)  
ra = 1500 - 0.5*n 
rb = 3000 - 3 * n

plt.plot(n, ra)
plt.plot(n, rb)
plt.axvline(x=800, color='green', linestyle='--', label='0.5*n + 0*r <= 400')
plt.xlabel('n')
plt.ylabel('r')
plt.grid(True)
plt.show()





