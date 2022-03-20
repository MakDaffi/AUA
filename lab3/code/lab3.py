import numpy as np

def task2(h):
    A = np.array([1, -2, -3 * h])
    ans = np.dot(A, A) + (10 - h / 2) * A + h / 2 * np.eye(2)
    print(ans)

if __name__ == "__main__":
    task2(2)