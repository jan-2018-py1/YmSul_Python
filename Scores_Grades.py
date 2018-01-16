import random

def yourGrade(x):
    grade = ""
    if x >= 60 and x <= 69:
        grade = 'D'
    if x >= 70 and x <= 79:
        grade = 'C'
    if x >= 80 and x <= 89:
        grade = 'B'
    if x >=90 and x <= 100:
        grade = 'A'
    print "Score: " + str(x) + "; Your grade is " + grade

print "Scores and Grades"
for i in range(0,10):
    random_num = random.randint(60,100)
    yourGrade(random_num)
print "End of the program. Bye!"
