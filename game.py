board = ["" for _ in range(9)]

def display_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("--|--|--")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("--|--|--")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

if __name__ == "__main__":
    print("〇×ゲームへようこそ！")
    display_board(board)