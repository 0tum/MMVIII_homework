import numpy as np

A = np.array([[1.0, 1.0, 3.0], [2.0, 1.0, 1.0], [1.0, 2.0, 1.0]])
x = np.array([1.0, 1.0, 1.0])

flag = True 

i = 0

while(max(np.dot(A, x) / x) / min(np.dot(A, x) / x) >= 1.0001):
    print("step", i)

    print("b/a:", max(np.dot(A, x) / x) / min(np.dot(A, x) / x))

    x = np.dot(A, x)
    print("x:", x)

    print("a:", min(np.dot(A, x) / x))
    
    i += 1

print("calculation finished.")
