import matplotlib.pyplot as plt
import numpy as np
# %% Zadanie 1

wektor = np.array([1,2,3,4,5])

print(wektor)

wektor[1] = -1
wektor[3] = wektor[3] * 2

print(wektor)


# %% Zadanie 2



macierz = np.random.randint(0,10,size=(3,4))
print("Macierz:")
print(macierz)
print("\n ---------------------------------------------------------------- \n")
print(macierz[1])
print("\n ---------------------------------------------------------------- \n")
print(macierz[:,1])
print("\n ---------------------------------------------------------------- \n")
macierz[0] *= 2
print(macierz)
print("\n ---------------------------------------------------------------- \n")
print(macierz[0:2,0:2])

# %% Zadanie 3

def simple_plot(a,b):

    x = np.arange(len(a))
    plt.plot(x,a, 'r--', label = " Wektor a")
    plt.plot(x,b, 'b-', label = " Wektor b")
    plt.title('Wykres porównawczy')
    plt.legend(loc='upper right')
    plt.xlabel("Oś X")
    plt.ylabel("Oś Y")
    plt.grid(alpha=0.5,linewidth=1.15, linestyle="--", color='green')
    plt.show()

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
simple_plot(a,b)


# %% Zadanie 4
def func_plot(vmin, vmax, step):
    x = np.arange(vmin, vmax, step)
    y = x**2 - x * 4 + 8

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Plot of f(x) = x^2 - x * 4 + 8')
    plt.grid(True)
    plt.show()


func_plot(-10, 10, 0.1)



# %% Zadanie 5
def multi_plot(sizes, labels):
    plt.subplot(1, 2, 1)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Pie Chart')

    plt.subplot(1, 2, 2)
    plt.bar(labels, sizes)
    plt.title('Bar Chart')

    plt.tight_layout()
    plt.show()


sizes = [1000000, 1500000, 2000000, 2500000]
labels = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław']

multi_plot(sizes, labels)

# %% Zadanie 6 

def scatter_plot():

    x = np.random.rand(1,100)
    y = np.random.rand(1,100)

    x2 = np.random.randn(1,100)
    y2 = np.random.randn(1,100)


    plt.scatter(x,y, color='blue',label="Group 1")
    plt.scatter(x2,y2, color='green', marker= '*', label="Group 2")
    plt.legend()
    plt.grid()
    plt.gca().set_axisbelow(True)
    plt.show()

scatter_plot()

# %% Zadanie 7

def make_3D(x, y):
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()


x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

make_3D(x, y)










