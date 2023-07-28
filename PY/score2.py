Stundets = []
Scores = []
st = int(input ("How many elements in students list: "))
sc = int(input ("How many scores for each element?"))

if st==sc:
    for i in range(st):
            strings = str(input ("Enter student name: "))
            Stundets.append(strings)
    print(Stundets)#for checking
    for j in range(sc):
            strings = str(input ("Enter student score: "))
            Scores.append(strings)
    print(Scores)#for checking
    print("Students and thair corresponding scores:\n" , dict(zip(Stundets,Scores)))
      
else:
    print("Error! Number of Student Names should be equal to number of their respective Score")