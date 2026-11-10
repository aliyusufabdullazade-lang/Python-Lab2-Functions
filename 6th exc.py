def average(*numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
def make_course(code, **details):
    course = {"code": code}
    for key in details:
        course[key] = details[key]
    return course
print(average(70, 80, 90))
print(average(100))
print(average())
print(make_course("CE101", title="Fundamentals of Programming", credits=6))
