import numpy as np
def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows, columns).tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    a = np.array(matrix)
    return a[row_start:row_stop, column_start:column_stop].tolist()

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    a = np.array(matrix).copy()
    a[row_start:row_stop, column_start:column_stop] = value
    return a.tolist()

def matrix_vector_product(matrix, vector):
    a = np.array(matrix)
    b = np.array(vector)
    return(a @ b).tolist()

def matrix_multiply(left, right):
    a = np.array(left)
    b = np.array(right)
    return(a @ b).tolist()

def transpose_matrix(matrix):
    a = np.array(matrix)
    a = np.array(matrix)
    b = np.array(vector)
    np.round(np.linalg.solve(a, b), 6).tolist()

def tensor_channel_mean(tensor):
    a = np.array(tensor)
    return a.mean(axis=-1).tolist()

def point_distance(first, second):
    a = np.array(first)
    b = np.array(second)
    return round(float(np.linalg.norm(a - b)), 6)
