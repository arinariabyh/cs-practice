def read_rows(lines):
    rows = []
    header = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        line2 = [x.strip() for x in line.split(',')]
        if not header:
            header = line2
            continue
        if len(line2) != len(header):
            continue
        row = {}
        for i in range(len(header)):
            row[header[i]] = line2[i]
        rows.append(row)
    return rows

def count_types(rows):
    counts = {}
    for row in rows:
        kind = row.get('тип')
        if kind is None:
            continue
        if kind in counts:
            counts[kind] += 1
        else:
            counts[kind] = 1
    return counts

def total_minutes(rows, kind):
    total = 0.0
    for row in rows:
        if row.get('тип') != kind:
            continue
        value = row.get('минуты', '').replace(',','.')
        try:
            total += float(value)
        except ValueError:
            continue
    return round(total, 1)

def to_csv(counts):
    result = 'тип,количество\n'
    for kind in sorted(counts):
        result += f'{kind},{counts[kind]}\n'
    return result
