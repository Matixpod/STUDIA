# %%
import matplotlib.pyplot as plt
import numpy as np
# %%
a = [1,2,3,4,5]
b = [6,7,8,9,10]

print(a+b)
print(a*2)
# print(a*b) błąd
print("\n================================\n")

a2 = np.array(a)
b2 = np.array(b)

print(a2+b2)
print(a2*2)
print(a2*b2)
print("\n================================\n")

print(a2.dtype)
print(a2.shape)
print("\n================================\n")

c = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(c.dtype)
print(c.shape)
print(c.size)
print("\n================================\n")

# %%

x = np.array([1,2,3,4,5,6])

x = np.linspace(-11,11,100)
y = np.sin(x)

plt.plot(x,y,"-",label="x,y")
plt.title("Title")
plt.legend(loc='upper left')
plt.grid(alpha=0.5, linestyle="--")
plt.xlabel("X axis label")
plt.ylabel("Y axis label")
plt.show()

print("\n================================\n")
# %%

