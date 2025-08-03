board = [" " for _ in range(9)]

def display_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

def handle_turn(player, board):
    """プレイヤーのターンを処理する関数"""
    print(f"\n{player} のターンです。")
    while True:
        try:
            position = int(input("どこに置きますか？ (1-9): "))
            if 1 <= position <= 9 and board[position - 1] == " ":
                board[position - 1] = player
                break
            else:
                print("その場所には置けません。")
        except ValueError:
            print("1から9の数字を入力してください。")

# メインの処理
if __name__ == "__main__":
    current_player = "X"
    print("〇×ゲームへようこそ！")

    # 9ターン繰り返すだけの仮のループ
    for _ in range(9):
        display_board(board)
        handle_turn(current_player, board)
        # プレイヤーを交代
        current_player = "O" if current_player == "X" else "X"

    print("\n最終的な盤面:")
    display_board(board)