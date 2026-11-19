
import numpy as np

#1

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

#2

print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])

#3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)
print("Элемент:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:", temperatures[:2, 1:])
print("Центральный фрагмент:", temperatures[:2, 1:3])


#4

matrix = np.arange(1, 26).reshape(5, 5)

part1 = matrix[:3, :]
print("Первые три строки:\n", part1)
print("shape:", part1.shape)

part2 = matrix[-2:, :]
print("Последние две строки:\n", part2)
print("shape:", part2.shape)

part3 = matrix[:, :2]
print("Первые два столбца:\n", part3)
print("shape:", part3.shape)

part4 = matrix[1:4, 2:5]
print("Фрагмент строк 1-3 и столбцов 2-4:\n", part4)
print("shape:", part4.shape)

part5 = matrix[-2:, -2:]
print("Правый нижний блок 2x2:\n", part5)
print("shape:", part5.shape)


#5

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("Изменённый vector:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("Изменённая small_matrix:\n", small_matrix)


changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("changed_hours:", changed_hours)
print("Исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("Изменённая матрица:\n", changed_matrix)
print("Исходная матрица:\n", matrix)


#6

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("numbers:\n", numbers)
print("table:\n", table)
print("transposed:\n", transposed)

print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)
