porog = float(input())
n = int(input())
errors = 0
excess = 0
summ = 0
mx = 0
count = 0
for i in range(n):
    g = input()
    if g == 'error':
        errors += 1
    else:
        g = float(g)
        count += 1
        if g > porog:
            excess += 1
        if count == 1:
            mx = g
        elif g > mx:
            mx = g
        summ += g
print(n)
print(errors)
print(excess)
print(f'{mx:.1f}')
print(f'{summ / count:.1f}')
