import numpy as np

a = np.random.randint(0, 11, (2, 2))
b = np.random.randint(0, 11, (2, 2))

print(a + b)
print(a - b)
print(3 * a)

print(np.dot(a, b))

m = np.random.randint(0, 11, (3, 3))
v = np.array([1, 0, -1])
print(np.dot(m, v))

z = np.eye(3)

c = np.diag([4,3,2])
zed = np.zeros((3,3))