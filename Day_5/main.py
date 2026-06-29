import art , random as rd
print(art.logo)
chances = 10
mode = input("Which mode do you want to play['easy' or 'hard']: ")
if mode == "hard":
    chances = 5
computer_guess = rd.randint(1,100)
user_guess = 0

print(f"You have {chances} chances")
while True:
    if chances == 0:
        print("You Lose")
        break
    user_guess = int(input("Guess a Number between 1 to 100: "))
    if user_guess == computer_guess:
        print(f"you won the number was {user_guess}")
        break
    else:
        if user_guess > computer_guess:
            print("To High.....")
        else:
            print("To Low......")
        chances-=1
    print(f"*****You have {chances} left*****")