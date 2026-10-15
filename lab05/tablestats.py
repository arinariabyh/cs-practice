def read_rows(lines):
    rows = []
    header = ''
    for line in lines:
        line = line.strip()
        line2 = [x.strip() for x in line.split(',')]
        if len(line) == 0:
            continue
        if header == '':
            header = line2
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
        type = row.get('тип')
        if type == None:
            continue
        if type in counts:
            counts[type] += 1
        else:
            counts[type] = 1
    return counts
