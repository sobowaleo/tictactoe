

def main():
    gamer = next_gamer("")
    spaces = game_board()
    while not (winner1(spaces) or is_a_draw(spaces)):
        show_board(spaces)
        make_a_move(gamer, spaces)
        gamer = next_gamer(gamer)
    show_board(spaces)
    print("Good game. Thanks for playing!") 

def game_board():
    spaces = []
    for square in range(9):
        spaces.append(square + 1)
    return spaces

def show_board(spaces):
    print()
    print(f"{spaces[0]}|{spaces[1]}|{spaces[2]}")
    print('-+-+-')
    print(f"{spaces[3]}|{spaces[4]}|{spaces[5]}")
    print('-+-+-')
    print(f"{spaces[6]}|{spaces[7]}|{spaces[8]}")
    print()
    
def is_a_draw(spaces):
    for square in range(9):
        if spaces[square] != "x" and spaces[square] != "o":
            return False
    return True 
    
def winner1(spaces):
    return (spaces[0] == spaces[1] == spaces[2] or
            spaces[3] == spaces[4] == spaces[5] or
            spaces[6] == spaces[7] == spaces[8] or
            spaces[0] == spaces[3] == spaces[6] or
            spaces[1] == spaces[4] == spaces[7] or
            spaces[2] == spaces[5] == spaces[8] or
            spaces[0] == spaces[4] == spaces[8] or
            spaces[2] == spaces[4] == spaces[6])

def make_a_move(gamer, board):
    square = int(input(f"{gamer}'s turn to choose a square (1-9): "))
    board[square - 1] = gamer

def next_gamer(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()