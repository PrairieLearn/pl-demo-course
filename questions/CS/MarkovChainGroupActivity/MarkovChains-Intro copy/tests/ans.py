import numpy as np
import numpy.linalg as la

def power_iteration(M, x):
    xc = x.copy()
    for _ in range(100):
        xc = M @ xc
    return xc

M_test = np.array([[0.3, 0.1], [0.7, 0.9]])
x_test = np.array([1.0, 0.0])
M_hidden = np.array([[0.4, 0.2], [0.6, 0.8]])
x_hidden = np.array([0.0, 1.0])
xc = power_iteration(M_test, x_test)
xc_hidden = power_iteration(M_hidden, x_hidden)

G = np.array([[1, 0.5,   0, 0],
              [0,   0, 0.5, 0],
              [0, 0.5,   0, 0],
              [0,   0, 0.5, 1]])

xstar2 = power_iteration(G, np.array([0.0, 0.0, 1.0, 0.0]))

A = np.array([[0,  2,  0,  5],
              [1,  0,  5,  6],
              [2,  4,  0,  3],
              [1,  0, 10,  2]])
n = len(A)
M2 = np.zeros((n, n))
for i in range(len(A[0])):
    M2[:,i] = A[:,i]/ la.norm(A[:,i],1)

num_pages = 20
edges = np.loadtxt("pagerank_large.txt").astype(np.int64)
A2 = np.zeros((num_pages, num_pages))
for edge in edges:
    A2[edge[1], edge[0]] = 1
M3 = A2.copy()
M3[:,la.norm(A2, 1, axis=0) == 0] = 1/num_pages
M3 /= la.norm(M3, 1, axis=0)