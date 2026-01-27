p1 = input("player1 enter your move  ").lower()
p2 = input("player2 enter your move  ").lower()
  

def play_rps(x,y):
    match (x, y):
        case (x, y) if x == y:
            return "tie"
        case ("rock", "scissor") | ("paper", "rock") | ("scissor", "paper"):
            return "p1 wins!"
        case ("scissor", "rock") | ("rock", "paper") | ("paper", "scissor"):
            return "p2 wins!"
        case _:
            return "Invalid input! Please use rock, paper, or scissor."
print(play_rps(p1,p2))
