import random

def number_guessing():
    print("------ NUMBER GUESSING GAME -------")
    print("\n CHOOSE A NUMBER BETWEEN 1-90")
    correct_num = random.randint(1,90)
    attempts = 0


    while True:
        guess = int(input("ENTER YOUR CHOICE : "))
        attempts += 1

        if attempts == 4:
            print("YOU RAN OUT OF ATTEMPTS :(")
            break
        else:
             if guess < correct_num:
               print("TO LOW !! TRY AGAIN...")
             elif guess > correct_num:
               print("TOO HIGH !! TRY AGAIN...")
             else:
               print("YAYYY !!!1 YOU WON THE GAME")


number_guessing()
