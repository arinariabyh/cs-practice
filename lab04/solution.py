def winner(names, scores):
    best_id = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[best_id]:
            best_id += 1
    return names[best_id]
def average(scores):
    if len(scores) == 0:
        return 0.0
    return round(sum(scores) / len(scores), 2)
print(average([]))
