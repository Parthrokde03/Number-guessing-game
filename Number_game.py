import random

def showMenu():
    print("=== Number Guessing Game ===")
    print("1.How to play")
    print("2.Play Game")
    print("3.Exit")
    print("\n")
    
    
while True:    
    showMenu()  
    choice = int(input("Enter your choice: "))  
    
    if choice == 1:
        print("How to play\n")
        print("1.The game will randomly generate a number within a specific range (e.g., 1 to 10).")
        print("2.You have 3 chances to guess this secret number.")
        print("3.If you guess the correct number within 3 tries — you win!")
        print("4.If all 3 guesses are wrong — the number is revealed, and the game ends.\n")
        print("\n")
    elif choice == 2:
        guessCount = 0  
        
        while guessCount < 3:
            yourGuess = int(input("Enter your guess: "))
            randomNumber = random.randrange(1,10)
            guessCount += 1 
            
            if yourGuess == randomNumber:
                print("You win")
                print(f"{yourGuess} = {randomNumber}")
                exit()
            print(f"Your guess {yourGuess} VS Random number {randomNumber}")      
                 
        print("You lose")
        #print(f"Your guess {yourGuess} and the random number {randomNumber} is different")
        exit()
                
    elif choice == 3:
        exit()    
    else:
        print("Invalid input")    
    