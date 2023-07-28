#ex1

"""studentsScore = {
    "Name_Student1":"John",
    "GradeStudent1":4 ,

    "Name_Student2":"Maria",
    "GradeStudent2": 5 ,

    "Name_Student3":"Zibi",
    "GradeStudent3": 3 ,
}

avarageGrade=((studentsScore["Score_Student1"] + studentsScore["Score_Student2"] + studentsScore["Score_Student3"])/3)
print (int(avarageGrade))"""

"""#listOfStudents =[
    {
    "Name_Student1":"John",
    "Grade":4 ,
    },
    {
    "Name_Student2":"Maria",
    "Grade": 5 ,
    },
    {
    "Name_Student3":"Zibi",
    "Grade":3
    }
]
"""


#print (listOfStudents[0])


"""for students in listOfStudents:
    #print("The student's name is:", students["Name_Student"+str((listOfStudents))])
    #print (students["Grade"])
    avarege += students["Grade"]
print (avarege/len(listOfStudents))"""


listOfStudents = []
numberOfStudens= int(input("How many students you want to register?: "))

for n in range(numberOfStudens):
    studentName = input("Student name:")
    studentGrade = input("Student grade:")
    stydentDictionary = {
        "Name": studentName,
        "Grade": int(studentGrade)
    }

    listOfStudents.append(stydentDictionary)
    print(listOfStudents)