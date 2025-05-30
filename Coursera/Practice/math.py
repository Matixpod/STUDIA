import numpy as np





v = np.array([-4,-3,8])
b1 = np.array([1,2,3])
b2 = np.array([-2,1,0])
b3 = np.array([-3,-6,5])
# b4 = np.array([0,0,0,3])

def wsp(a,b):
    return a@b / np.sum(b**2)

r1 = wsp(v,b1)
r2 = wsp(v,b2)
r3 = wsp(v,b3)
# r4 = wsp(v,b4)
vb = (np.array([r1,r2,r3]))

# print(vb)

# s = np.array([2,1])
# k = np.array([3,-4])

# print(s@k/np.sqrt(np.sum(k**2)))


s = np.array([[4/13]
            ,[-3/13]
            ,[-12/13]])

r = [[6]
    ,[2]
    ,[3]]

s1 = (s[0]/s[2])[0]
s2 = (s[1]/s[2])[0]

A = np.array([[1,0,-s1]
            ,[0,1,-s2]])

R = np.array([[5,-1,-3,7],
            [4,-4,1,-2],
            [9,3,0,12]])
# print(A)
# print(r-s*(r[2]/s[2]))
print(np.round(A @ R,3))




