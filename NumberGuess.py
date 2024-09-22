import random

top_of_range = input("Type a Number: ")

random_number = random.randint(1,11)

if top_of_range.isnumeric():
    top_of_range = int(top_of_range) 
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time..')
        quit()
else:
    print("Please type a number next time..")
    quit()

random_number = random.randint(0,top_of_range)
print(random_number)
guesses = 0
max_guess = 0 

while True:
    guesses += 1
    max_guess = 10
    user_guess = input("Make a guess:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    if user_guess == random_number:
        print("you got it in ",guesses,"guesses")
        break
    elif(guesses == max_guess):
            print("sorry! you exceed the guess ...")
            print("you did not got it ...")
            break
    else:
        if user_guess > random_number:
            print("you were above the number!")
        else:
            print("you were below the number")
        

