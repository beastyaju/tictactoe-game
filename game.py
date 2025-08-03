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

def check_winner(board):
    """勝者をチェックする関数"""
    # 勝利パターン
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 横
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 縦
        [0, 4, 8], [2, 4, 6]             # 斜め
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != " ":
            return board[condition[0]]  # 勝者 ('X' or 'O') を返す
    
    # 引き分けのチェック (盤面が埋まっているか)
    if " " not in board:
        return "Draw" # 引き分け
        
    return None

# メインの処理
if __name__ == "__main__":
    current_player = "X"
    winner  = None
    print("〇×ゲームへようこそ！")

    # 9ターン繰り返すだけの仮のループ
    while not winner:
        display_board(board)
        handle_turn(current_player,board)
        winner = check_winner(board)

        if not winner:
            current_player = "0" if current_player == "X" else "X"
    
    display_board(board)
    if winner == "Draw":
        print("\n引き分けです")
    else:
        print(f"\nおめでとう！{winner}の勝ちです！")
