

def play_rps():
     x = input("player1 enter your move  ").lower()
     y = input("player2 enter your move  ").lower()
     match (x, y):
        case (x, y) if x == y:
            print("tie") 
        case ("rock", "scissor") | ("paper", "rock") | ("scissor", "paper"):
            print("p1 wins!") 
        case ("scissor", "rock") | ("rock", "paper") | ("paper", "scissor"):
            print("p2 wins!")
        case _:
            print("Invalid input! Please use rock, paper, or scissor.")
  
choice = "yes"
while(choice=="yes"):
    play_rps()
    choice = input("Do you want to continue").lower()


