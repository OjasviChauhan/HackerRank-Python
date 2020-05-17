n = int(input())
student_marks = {}              #Creating a empty dictionary
for i in range(n):
    line = input().split()
    name = line[0]
    marks = line[1:]
    avg = (float(marks[0])+float(marks[1])+float(marks[2]))/3
    student_marks[name] = format(avg, '.2f')  #here, first converting avg unto 2-decimal number and then storing into it's coresponding key
    
student = input()
print(student_marks[student])
