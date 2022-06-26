import random
def guess(x):
    random_number = random.randint(1, x)
    g=0
    while g!=random_number:
        g=int(input(f"Guess a number from 1 to {x}: "))
        if g < random_number:
            print("Sorry,guess again. Too low. ")
        elif g > random_number:
            print("Sorry,guess again. Too high.")
    print(f"Yayy!! you have guessed the number {random_number} correctly!!")

guess(10)




