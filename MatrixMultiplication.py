import numpy as np


def matrix_multiply(A: np.ndarray, B: np.ndarray, C: np.ndarray, size: int):
    for i in range(size):
        for j in range(size):
            for k in range(size):
                C[i][j] += A[i][k] * B[k][j]


def matrix_multiply_r(A: np.ndarray, B: np.ndarray, C: np.ndarray, size: int):
    matrix_multiply_recursive(A, B, C, size, (size, size), (size, size), (size, size))


def matrix_multiply_recursive(A: np.ndarray, B: np.ndarray, C: np.ndarray, size: int, a: tuple, b: tuple, c: tuple):
    print(a)
    print(b)
    print(c)
    if size == 0:
        C[c[0]][c[1]] += A[a[0]][a[1]] * B[b[0]][b[1]]
    else:
        matrix_multiply_recursive(A, B, C, size // 2, (a[0] // 2, a[1] // 2), (b[0] // 2, b[1] // 2), (c[0] // 2, c[1] // 2))
        matrix_multiply_recursive(A, B, C, size // 2, (a[0] // 2, a[1]), (b[0], b[1] // 2), (c[0] // 2, c[1] // 2))
        matrix_multiply_recursive(A, B, C, size // 2, (a[0] // 2, a[1] // 2), (b[0] // 2, b[1]), (c[0] // 2, c[1]))
        matrix_multiply_recursive(A, B, C, size // 2, (a[0] // 2, a[1]), (b[0], b[1]), (c[0] // 2, c[1]))
        matrix_multiply_recursive(A, B, C, size // 2, (a[0], a[1] // 2), (b[0] // 2, b[1] // 2), (c[0], c[1] // 2))
        matrix_multiply_recursive(A, B, C, size // 2, (a[0], a[1]), (b[0], b[1] // 2), (c[0], c[1] // 2))
        matrix_multiply_recursive(A, B, C, size // 2, (a[0], a[1] // 2), (b[0] // 2, b[1]), (c[0], c[1]))
        matrix_multiply_recursive(A, B, C, size // 2, (a[0], a[1]), (b[0], b[1]), (c[0], c[1]))


if __name__ == '__main__':
    n = 3
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    C = np.zeros((n, n), dtype=int)
    matrix_multiply_r(A, B, C, n-1)
    print(C)
