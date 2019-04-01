in_play = 'y'

start_number = 1

while in_play == 'y':
    user_number = input("How many numbers? ")

    for x in range(start_number, start_number + int(user_number)):
        print(x)

    start_number = x

    in_play = input("Continue the chain? (y)es or (n)o: ")
