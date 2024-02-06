import random
#0. Count numbers
'''
number = -10
while number <= 10:
    print(number)
    number += 1
'''
#1. Arithmetic sum
'''
number = 1
sum = 0


while number <= 100:
    sum += number  
    number += 1  

print(sum)

number = 1
sum = 0


while number <= 100:
    sum += number  
    number += 2  

print(sum)
'''

#2. Guess the number game
#a)
'''
random_number = random.randint(1, 100)
attempts = 0
while True:
    print(random_number)
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1
    if guess < random_number:
        print(f"Your guess {guess} was to low, try again!")
    elif guess > random_number:
        print(f"Your guess {guess} was to high, try again!")
        
    else:    
        print(f"Your guess {guess} is correct, congratulations!!. It took you {attempts} tries")
        break
'''
#b)

'''
lowest = 1
highest = 100
number = random.randint(lowest, highest)
attempts = 0
low = lowest
high = highest

print(f"{number}")  

while low <= high:
    guess = (low + high) // 2
    attempts += 1
    if guess < number:
        print(f"Guess #{attempts}: {guess} is too low.")
        low = guess + 1
    elif guess > number:
        print(f"Guess #{attempts}: {guess} is too high.")
        high = guess - 1
    else:
        print(f"Guess #{attempts}: {guess} is correct!")
        break

print(f"guessed the correct number {number} in {attempts} guesses.")
'''

#3. Multiplication game
# a, b)
'''
def Choice_one():
    while True:
        random_x = random.randint(1,10)
        random_y = random.randint(1,10)
        correct_answer = random_x * random_y
        
        print(f"What is {random_x} x {random_y}?")
        answer = int(input("Guess: "))
        if answer == correct_answer:
            print(f"Your answer {answer} is correct!")
        else:
            print(f"Sorry its wrong the correct answer is {correct_answer}")
        
        Again = input("want to play again? (yes/no): ")
        if Again.lower() == "no":
            print("Thanks for playing, going back to main menu.")
            break
        
        
def Choice_two():
    
    while True:
        random_x = random.randint(1,100)
        random_y = random.randint(1,100)
        correct_answer = random_x * random_y
        
        print(f"What is {random_x} x {random_y}?")
        answer = int(input("Guess: "))
        if answer == correct_answer:
            print(f"Your answer {answer} is correct!")
        else:
            print(f"Sorry its wrong the correct answer is {correct_answer}")
        
        Again = input("want to play again? (yes/no): ")
        if Again.lower() == "no":
            print("Thanks for playing, going back to main menu.")
            break
        
def Choice_three():
    
    while True:
        random_x = random.randint(1,100)
        random_y = random.randint(1,100)
        correct_answer = random_x * random_y
        
        print(f"What is {random_x} x {random_y}?")
        answer = int(input("Guess: "))
        if answer == correct_answer:
            print(f"Your answer {answer} is correct!")
        else:
            print(f"Sorry its wrong the correct answer is {correct_answer}")
        
        Again = input("want to play again? (yes/no): ")
        if Again.lower() == "no":
            print("Thanks for playing, going back to main menu.")
            break
   


while True:
        print("\nMain Menu")
        print("1 - 1-10 muliplicative")
        print("2 - 1-100 muliplicative")
        print("3 - 1-1000 muliplicative")
        print("4 - Avsluta programmet")
        
        Choice = input("Please choose difficulty level: ")
        
        if Choice == '1':
            Choice_one()
        elif Choice == '2':
            Choice_two()
        elif Choice == '3':
            Choice_three()
        elif Choice == '4':
            print("Tack för att du använde programmet. Hejdå!")
            break
        else:
            print("Felaktig inmatning, vänligen välj ett nummer mellan 1 och 4.")
'''
#4. Check convergence

#????

