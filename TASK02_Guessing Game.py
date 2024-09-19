import random
num=random.randint(1,101)
chance=0
while True:
    chance+=1
    try:
        user_input = int(input("Guess the Number: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    if user_input<num:
        if num-user_input<=10:
            print("Very close, but it's a bit higher!")
        else:
            print("Too Low! Try again.")
    elif user_input>num:
        if user_input-num<=10:
            print("Very close, but it's a bit lower!")
        else:
            print("Too High! Try again.")
    else:
        print(f"Yoo! You guessed the right number: {num} in {chance} chances.")
        break