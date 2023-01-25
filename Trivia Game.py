print("Quiz Game")

name = input(str("Enter your name: "))
print("Welcome to the quiz" + " " +name )
score = 0

stars = "************************************************************"

print("Choice 1> Start Quiz")
print("Choice 2> View Score")
print("Choice 3> Exit Quiz")
choice = int(input("Enter your choice: "))

print(stars)

score = 0

if(choice == 1):

    answer = input("Kosovo is located on one of Europe's major peninsulas. On which peninsula can it be found? \n a) Scandinavian Peninsula b) Balkan Peninsula \n c) Italian Peninsula d) Iberian Peninsula \n Enter Your Select Answer: ")
if answer.lower() == "b":
    print("Your answer is Correct")
    score +=1
else: print("Your answer is Wrong!")

print(stars)


answer = input("On which of these seas does Kosovo have a coastline? \n a) Black Sea b) None of them - Kosovo is landlocked, and has no coastline \n c) Adriatic Sea d) Aegean Sea \n Enter Your Select Answer: ")
if answer.lower() == "b":
    print("Your answer is Correct")
    score +=1
else: print("Your answer is Wrong!")

print(stars)

answer = input("The Capital and largest city of Kosovo, Pristina, used to have a river flowing through it. What happened to the Pristevka River during the 1950s?  \n a) It was dammed to provide electricity for Pristina. b) A major landslide changed the course of its flow in 1956. \n c) It was diverted for irrigation in the Metohija basin. d) It was diverted to underground tunnels. \n Enter Your Select Answer: ")
if answer.lower() == "d":
    print("Your answer is Correct")
    score +=1
else: print("Your answer is Wrong!")

print(stars)


answer = input("Which colors are there in the flag of Kosovo? \n a) Blue, Yellow and White b) Red and Black \n c) Red, Blue and White d) Red and White \n Enter Your Select Answer: ")
if answer.lower() == "a":
    print("Your answer is Correct")
    score +=1
else: print("Your answer is Wrong!")

print(stars)

answer = input("Where was Adem Jashari Born? \n a) Prishtina b) Likovic \n c) Kizhnareka d) Prekaz \n Enter Your Select Answer: ")
if answer.lower() == "d":
    print("Your answer is Correct")
    score +=1
else: print("Your answer is Wrong!")

print(stars)

answer = input("Rita was named after actress Rita Hayworth as her grandfather was a huge fan? \n a) True b) False \n Enter Your Select Answer: ")
if answer.lower() == "a":
    print("Your answer is Correct")
    score +=1
else: print("Your answer is Wrong!")

print(stars)

print("Choice 1> Start Quiz")
print("Choice 2> View Score")
print("Choice 3> Exit Quiz")
choice = int(input("Enter your choice: "))

print(stars)

if(choice == 2):
    print("You got " + str(score) + " questions correct!")
    print("You got " + str(6-score) + " questions wrong!")
    print("Your Score", str(score))
    print ("Your percentage = ",round((score/6)*100),"%.")

print(stars)

print("Choice 1> Start Quiz")
print("Choice 2> View Score")
print("Choice 3> Exit Quiz")
choice = int(input("Enter your choice: "))

print(stars)


if(choice==3):
    print("Quiz Stopped")
    quit()








    






