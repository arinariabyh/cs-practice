import numpy as np
def reshape_rows(values, width):
    if width <= 0 or len(values) % width != 0:
        return []
    array = np.asarray(values, dtype=float)
    return array.reshape(-1, width).tolist()

def block(matrix, rows, columns):
    array = np.asarray(matrix, dtype=float)
    if array.size == 0:
        return []
    return array[np.ix_(rows, columns)].tolist()

