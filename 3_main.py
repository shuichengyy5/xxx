#202410111303
#3331592296@qq.com
#余洋
def print_chess(chess):
    for solution in chess:
        for line in solution:
            print(line,end="")
        print()
    print()

def is_safe(board,row,arr,n):
    for i in range(row):
        if board[i][arr]=='Q':
            return False
    for i,j in zip(range(row,-1,-1),range(arr,-1,-1)):
        if board[i][j]=='Q':
            return False
    for i,j in zip(range(row,-1,-1),range(arr,n)):
        if board[i][j]=='Q':
            return False
    return True

def place_queens_util(board, row, n, chess):
    if row == n:
        solution = [['.' if x == ',' else x for x in row] for row in board] 
        solution_str = [['' if x == '.' else 'Q' for x in row] for row in solution] 
        solution_str_rep = [['.' if x == '' else 'Q' for x in row] for row in solution_str] 
        chess_str = [[''.join(row) for row in solution_set] for solution_set in [solution_str_rep]] 
        chess.append(chess_str[0])  
        return
    for arr in range(n):
        if is_safe(board, row, arr, n):
            board[row][arr] = 'Q'
            place_queens_util(board, row + 1, n, chess)
            board[row][arr] = ','  

def place_queens(n):
    board=[['.' for _ in range(n)]for _ in range(n)]
    chess=[]
    place_queens_util(board,0,n,chess)
    return chess

input_n=int(input(""))
chess=place_queens(input_n)
print_chess(chess)
