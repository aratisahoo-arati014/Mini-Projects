print("Welcome to my computer quiz!")

playing = input(" Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("--------okay! Let's play :---------")
score = 0
answer = input("what does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect! ")

answer = input("what does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect! ")

answer = input("what does RAM stands for? ")
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print("Incorrect! ")

answer = input("what does PSU stands for? ")
if answer.lower() == "power supply unit":
    print('correct!')
    score += 1
else:
    print("Incorrect! ")

print("Total score is ",str(score),"out of 4..")
print("you got ",str((score/4)*100),"%")

