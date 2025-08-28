import random

random_number = random.randint(1, 100)
count = 0
score = 100

while True:
    user_input = int(input("Enter the number(1-100): "))
    count += 1

    if user_input < random_number:
        print("too low")

    elif user_input > random_number:
        print("too High")

    else:
        print(f"You are correct and the number is {random_number}")
        print(f"Your score is {score}")
        break

    score -= 10

    if count >= 10:
        print("You are out of attempts and your score is 0")
        print(f"The correct number was {random_number}")
