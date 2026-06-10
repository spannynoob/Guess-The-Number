import random

atpts = None
GREEN = "\033[32m"
RESET = "\033[0m"

banner = r"""

  ██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
 ██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
 ██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║█████╗      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
 ██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══╝      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
 ╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

"""

# --- GAME MODES & MENUS (Defined First) ---

def types():
    while True:
        print("\n" + "="*20)
        print("1. Rush Mode")
        print("2. Carrier Mode")
        print("3. Levels Mode")
        print("4. Back to Main Menu")
        print("="*20)
        
        mode_choice = input("Select a game mode (1-4): ").strip()
        
        if mode_choice =='1':
            RushMode()
        elif mode_choice == '2':
            CarrierMode()
        elif mode_choice =='3':
            LevelsMode()
        elif mode_choice == '4':
            break
        else:
            print("Invalid Choice! Please try again.")

def CarrierMode():
    global atpts
    
    while True:
        guess = random.randint(1,20)
        attempts=0
        print("I think of a number.. can u guess it?")
        
        while True:
            guess_pl = int(input("Take a guess: "))
            attempts += 1
            
            if guess_pl < guess:
                print("Too low!! Guess a higher number")
            elif guess_pl > guess:
                print("Too High!! Try a lower number")
            else:
                print("Good job, you guessed it right!! Level 1 Passed!!")
                
                if atpts is None or attempts < atpts:
                    atpts = attempts
                    print(f"🎉New Best Score recorded: {atpts} attempts!")
                break
                    
        play = input("\nDo you want to play again? (Y/N): ").strip().lower()
        if play not in ['yes', 'y']:
            print("Thanks for playing! Goodbye.")
            break
            
def RushMode():
    print("\n----------RUSH MODE----------")
    print("Be Smart, you only have 5 attempts")
    guess = random.randint(1,20)
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        guess_pl = int(input(f"Attempt {attempts + 1}/{max_attempts} - Take a guess: "))
        attempts += 1
        
        if guess_pl < guess:
            print("Too low!!")
        elif guess_pl > guess:
            print("Too high!!")
        else:
            print(f"Boom! You beat the Rush Mode in {attempts} attempts!")
            return
    
    print(f"Game Over! You ran out of shots. The correct number was {guess}.")

def LevelsMode():
    print("\n----------LEVELS MODE----------")
    level = 1
    max_range = 10
    
    while level <= 3:
        print(f"\n----------LEVEL {level}----------")
        print(f"Guess the number between 1 and {max_range}.")
        guess = random.randint(1, max_range)
        
        while True:
            guess_pl = int(input("Take a guess: "))
            if guess_pl < guess:
                print("Too low!!")
            elif guess_pl > guess:
                print("Too High!!")
            else:
                print(f"Level {level} cleared!")
                break
        level += 1
        max_range *= 5
        
    print("\nCongratulations! You conquered all levels!")

# --- MAIN EXECUTION LOOP (Moved to the Bottom) ---

while True:
    print(f"{GREEN}{banner}{RESET}")
    print("\n" + "="*20)
    print("1. Start Game")
    print("2. Exit")
    print("3. Best Score")
    print("="*20)
    
    menuchoice = input("Select an option (1, 2, 3): ").strip()
    
    if menuchoice == '1':
        types()
    elif menuchoice == '2':
        print("Thanks for playing!! Goodbye")
        break
    elif menuchoice == '3':
        if atpts is None:
            print("\nNo best score recorded yet! Play Carrier Mode first")
        else:
            print(f"\nYour Best Score is {atpts} attempts!")
    else:
        print("Invalid Choice! Please choose again!")