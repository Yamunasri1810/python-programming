import numpy as np
a = np.array([[1,8,3,21,5],[11,12,13,14,15]])
b = np.array([[[6,7,8,9,10],[16,17,18,19,20]], [[1,2,3,4,5],[11,12,13,14,15]]])
c = np.array([[21,22,23,24,25], [31,32,33,34,35]])
print(f'a = {a}')
print(f'b = {b}')
print(np.ndim(a))
print(np.ndim(b))
print(np.shape(a))
print(np.shape(b))
print(np.reshape(a,(5,2)))
print(np.ones((3,3),dtype = 'int'))
print(np.zeros((3,3), dtype = 'int'))
print(np.full((3,3), 6))
print(np.eye(3,3))
print(np.sort(a, axis = 0))
print(np.max(a, axis = 0))
print()
print()
print("___________________________________________________")
print(np.concatenate((a,c)))
print(np.linspace(0,10,2, endpoint = True, retstep= True))
print(np.logspace(0,10))
print(np.stack((a,c)))
print(np.stack((a,c), axis = 1))
print(np.dstack((a,c)))
print(np.split(a,2))
print(np.array_split(a,3))
print(np.where(a==14))
print(np.searchsorted(a, [2,9]))
