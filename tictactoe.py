import random

def print_board(board):
    print("\n")
    for row in range(3):
        print(f" {board[row*3]} | {board[row*3+1]} | {board[row*3+2]} ")
        if row<2:
            print("---|---|---")
    print("\n")

def check_winner(board,player):
    win_condn=[
        [0, 1, 2],[3, 4, 5],[6, 7, 8],
        [0, 3, 6],[1, 4, 7],[2, 5, 8],
        [0, 4, 8],[2, 4, 6]
    ]
    for condn in win_condn:
        if board[condn[0]]==board[condn[1]]==board[condn[2]]==player:
            return True
    return False

def isFull(board):
    return ' ' not in board

def tic_tac_toe():
    board=[' '] * 9
    print("Welcome to Tic-Tac-Toe!")
    
    human_symbol=''
    while human_symbol not in ['X','O']:
        human_symbol=input("Choose your symbol (X or O): ").strip().upper()
        if human_symbol not in ['X','O']:
            print("Invalid choice! Please type 'X' or 'O'.")
            
    computer_symbol='O' if human_symbol == 'X' else 'X'
    print(f"\nYou are playing as '{human_symbol}'.The computer will be '{computer_symbol}'.")
    
    print("\nBoard positions are 1 through 9 as shown below:")
    print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 ")

    current_player = 'X'
    
    while True:
        print_board(board)
        
        if current_player == human_symbol:
            try:
                move = int(input(f"Your turn ({human_symbol}). Enter position (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != ' ':
                    print("Invalid move! Pick an empty slot from 1 to 9.")
                    continue
            except ValueError:
                print("Please enter a valid integer (1-9).")
                continue
        else:
            print(f"Computer's turn ({computer_symbol})...")
            available_moves = [i for i in range(9) if board[i] == ' ']
            move = random.choice(available_moves)
            
        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            if current_player == human_symbol:
                print("Congratulations! You won!")
            else:
                print("Computer won!")
            break
            
        if isFull(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = computer_symbol if current_player == human_symbol else human_symbol

if __name__ == "__main__":
    tic_tac_toe()

