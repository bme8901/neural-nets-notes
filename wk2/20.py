import numpy as np

# Rank 1 array vs.
# a = np.random.randn(5, 1)
# which is a column vector.
a = np.random.randn(5)

print(a.shape)
print(a.T)
print(np.dot(a, a.T))

# Uncomment line 4 and comment line 6 above for this to pass
assert(a.shape == (5,1))