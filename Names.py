# Part 1:
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def DictStudents(info):
    for value in info:
        print value['first_name'], value['last_name']

DictStudents(students)

# Part 2:
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
 
def doubleDictReader(some_info):
    idNum = 1 #initialize variable
    for key in some_info:
        print key
        for value in some_info[key]:
            print "{} - {} {} - {}".format(idNum, value['first_name'], value['last_name'], len(value['first_name'])+len(value['last_name']))
            idNum += 1
        idNum = 1 #reset for next dict

doubleDictReader(users)
