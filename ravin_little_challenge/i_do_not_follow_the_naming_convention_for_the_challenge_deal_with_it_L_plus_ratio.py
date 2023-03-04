playerOne = int(input("P1: enter a number: "))
if playerOne <= 50 and playerOne >= 1:
    difficulty = input("difficulty [easy, medium, hard]")
    match difficulty.lower().strip():
        case "easy":
            guesses = 8
            while True:
                playerTwo = int(input("P2: enter your geuss: "))
                if playerTwo == playerOne:
                    print("You guessed the correct number")
                    break
                else:
                    print("you did not guess the correct number")
                    guesses -= 1
                    if guesses == 0:
                        print("game over")
                        break            
        case "medium":
            guesses = 5
            while True:
                playerTwo = int(input("P2: enter your geuss: "))
                if playerTwo == playerOne:
                    print("You guessed the correct number")
                    break
                else:
                    print("you did not guess the correct number")
                    guesses -= 1
                    if guesses == 0:
                        print("game over")
                        break
        case "hard":
            guesses = 3
            while True:
                playerTwo = int(input("P2: enter your geuss: "))
                if playerTwo == playerOne:
                    print("You guessed the correct number")
                    break
                else:
                    print("you did not guess the correct number")
                    guesses -= 1
                    if guesses == 0:
                        print("game over")
                        break
