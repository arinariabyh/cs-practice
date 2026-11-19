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

def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []
    array = np.asarray(matrix, dtype=float)
    return np.round(array.mean(axis=0), 6).tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return 0.0

    array = np.asarray(matrix, dtype=float)
    result = array[:, column].max() - array[:, column].min()
    return round(float(result), 6)