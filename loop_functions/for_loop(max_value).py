# maximum score
student_score = [110, 120, 130, 140 , 100, 90, 123, 156, 145, 170, 163, 190, 187, 200, 1999, 199, 999]
max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score
print(max_score)