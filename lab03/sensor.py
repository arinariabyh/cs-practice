porog = int(input())
n = int(input())
errors = 0
excess = 0
summ = 0
mx = 0
for i in range(n):
    g = input()
    if g == 'error':
        errors += 1
    else:
        g = float(g)
        if g > porog:
            excess += 1
        if g > mx:
            mx = g
        summ += g
print(n)
print(errors)
print(excess)
print(f'{mx:.1f}')
print(f'{summ/(n - errors):.1f}')
