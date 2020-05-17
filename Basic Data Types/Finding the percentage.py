n = int(input())
student_marks = {}
for i in range(n):
    line = input().split()
    name = line[0]
    marks = line[1:]
    avg = (float(marks[0])+float(marks[1])+float(marks[2]))/3
    student_marks[name] = format(avg, '.2f')
    
student = input()
print(student_marks[student])
