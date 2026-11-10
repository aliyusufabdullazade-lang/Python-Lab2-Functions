def add_bonus(scores, bonus):
    for i in range(len(scores)):
        scores[i] = min(scores[i] + bonus, 100)
def with_bonus(scores, bonus):
    result = []
    for s in scores:
        result.append(min(s + bonus, 100))
    return result
scores = [70, 95, 88, 100]
print(with_bonus(scores, 10))
print(scores)
add_bonus(scores[:], 10)
print(scores)
add_bonus(scores, 10)
print(scores)
