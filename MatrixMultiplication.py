import numpy as np


def matrix_multiply(A: np.ndarray, B: np.ndarray, C: np.ndarray, size: int):
    for i in range(size):
        for j in range(size):
            for k in range(size):
                C[i][j] += A[i][k] * B[k][j]


def matrix_multiply_r(A: np.ndarray, B: np.ndarray, C: np.ndarray, size: int):
    matrix_multiply_recursive(A, B, C, size, (size, size), (size, size), (size, size))


def matrix_multiply_recursive(A: np.ndarray, B: np.ndarray, C: np.ndarray, size: int, a: tuple, b: tuple, c: tuple):
    if size == 1:
        C[c[0] - 1][c[1] - 1] += A[a[0] - 1][a[1] - 1] * B[b[0] - 1][b[1] - 1]
    else:
        half_size = size // 2
        matrix_multiply_recursive(A, B, C, half_size, (a[0] - half_size, a[1] - half_size), (b[0] - half_size, b[1] - half_size), (c[0] - half_size, c[1] - half_size))
        matrix_multiply_recursive(A, B, C, half_size, (a[0] - half_size, a[1]), (b[0], b[1] - half_size), (c[0] - half_size, c[1] - half_size))
        matrix_multiply_recursive(A, B, C, half_size, (a[0] - half_size, a[1] - half_size), (b[0] - half_size, b[1]), (c[0] - half_size, c[1]))
        matrix_multiply_recursive(A, B, C, half_size, (a[0] - half_size, a[1]), (b[0], b[1]), (c[0] - half_size, c[1]))
        matrix_multiply_recursive(A, B, C, half_size, (a[0], a[1] - half_size), (b[0] - half_size, b[1] - half_size), (c[0], c[1] - half_size))
        matrix_multiply_recursive(A, B, C, half_size, (a[0], a[1]), (b[0], b[1] - half_size), (c[0], c[1] - half_size))
        matrix_multiply_recursive(A, B, C, half_size, (a[0], a[1] - half_size), (b[0] - half_size, b[1]), (c[0], c[1]))
        matrix_multiply_recursive(A, B, C, half_size, (a[0], a[1]), (b[0], b[1]), (c[0], c[1]))


if __name__ == '__main__':
    n = 4
    A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    B = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    C = np.zeros((n, n), dtype=int)
    matrix_multiply_r(A, B, C, n)
    print(C)
