from random import randint

def validate_move(player_score,program_score):
    while True:
        player = input("rock, paper, scissors? ")
        options = ["rock", "paper", "scissors"]
        program = options[randint(0,2)]
        print(program)
        if player == program:
            print("Tie game")
            player_score += 1
            program_score += 1
        elif player == "rock":
            if program == "paper":
                print("player lost!", program, "covers", player)
                program_score += 1
            else:
                print("player won!", player, "smashes", program)
                player_score += 1
        elif player == "paper":
            if program == "scissors":
                print("player lost!", program, "cut", player)
                program_score += 1
            else:
                print("player won!", player, "covers", program)
                player_score += 1
        elif player == "scissors":
            if program == "rock":
                print("player lost!", program, "smashes", player)
                program_score += 1
            else:
                print("player won!", player, "cut", program)
                player_score += 1
        else:
            print("Invalid input")
        play_again = input("Wanna play again? press(y,n): ")
        print()
        if play_again.lower() != "y":
            break
    print("score of player = ",player_score)
    print("score of program = ",program_score)

def score():
    player_score = 0
    program_score = 0
    validate_move(player_score,program_score)
score()
    
