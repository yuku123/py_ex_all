import numpy as np

a = np.mat(np.array([1,2,3]))
print(a)

b = a.transpose()

c = b*a
print(c)

d = np.linalg.det(c)

c= np.mat(np.array([[1,3,3],[2,2,3],[1.1,2,3.1]]))
e = np.linalg.inv(c)
print(e)

print(e*c)