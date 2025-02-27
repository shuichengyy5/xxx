#202410111303
#3331592296@qq.com
#余洋
def input_board(input_str):
        arrays=input_str.split('/')
        board=[]
        for array in arrays:
            row=list(map(int,array.split(',')))
            board.append(row)

def maxSumOfThreeCars(board):
    m, n = len(board), len(board[0])
    max_sum = float('-inf')

    def is_safe(row, col, placed):
        for r, c in placed:
            if r == row or c == col:
                return False
        return True

    def calculate_max(row, col, count, placed, current_sum):
        nonlocal max_sum
        if count == 3:
            max_sum = max(max_sum, current_sum)
            return
        if row == m:
            return
        if col == n:
            calculate_max(row + 1, 0, count, placed, current_sum)
            return
        if is_safe(row, col, placed):
            calculate_max(row,col+1,count,placed,current_sum)
            calculate_max(row+1, 0, count + 1, placed + [(row, col)], current_sum + board[row][col])
            calculate_max(row+1,col,count,placed,current_sum)

    def input_board(input_str):
        arrays=input_str.split('/')
        board=[]
        for array in arrays:
            row=list(map(int,array.split(',')))
            board.append(row)
        return board

input_str=input("")
board=input_board(input_str)
result= maxSumOfThreeCars(board)
print(result)
