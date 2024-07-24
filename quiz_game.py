print("Welcome to my computer quiz ")

playing = input("Do you want to play my Game? : ")
if playing.lower() != "yes":
    quit()
print("Okey have a fun then:)")
score = 0


answer = input("What does CPU satands for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What does GPU Stands for? ")
if answer.lower() == "graphics standards unit":
    print("Correct")
    score += 1

else:
    print("Incorrect")
answer = input("What does RAM Stands for ?")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What does IP stamnds for? ")
if answer.lower() == "internet protocal":
    print("Correct")
    score += 1
else:
    print("Incorrect")
print("You got " + str(score) + " Questions Correct!")
print("You got " + str((score/4)*100) + "%.")
