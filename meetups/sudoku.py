import copy

def is_valid(board, num, row, col):
  if num in board[row]:
    return False
  for check_row in range(len(board)):
    if board[check_row][col] == num:
      return False
  if 0 <= row <= 2:
    row_sq = [0, 3]
  elif 3 <= row <= 5:
    row_sq = [3, 6]
  else:
    row_sq = [6, 9]
  if 0 <= col <= 2:
    col_sq = [0, 3]
  elif 3 <= col <= 5:
    col_sq = [3, 6]
  else:
    col_sq = [6, 9]
  for row_index in range(row_sq[0], row_sq[1]):
    for col_index in range(col_sq[0], col_sq[1]):
      if board[row_index][col_index] == num:
        return False
  return True

def recurse_sudoku(board, solution, row, col):
  if row > 8:
    for app_row in range(len(board)):
      solution.append(copy.deepcopy(board[app_row]))
    return
  else:
    if col == 8:
      new_row, new_col = row + 1, 0
    else:
      new_row, new_col = row, col + 1
    if board[row][col] != ".":
      recurse_sudoku(board, solution, new_row, new_col)
    else:
      for num in range(1, 10):
        number = str(num)
        if is_valid(board, number, row, col):
          board[row][col] = number
          recurse_sudoku(board, solution, new_row, new_col)
          board[row][col] = "."

def solve_sudoku(board):
  solution = []
  recurse_sudoku(board, solution, 0, 0)
  return solution


board = [[".",".",".",".",".",".",".","7","."],["2","7","5",".",".",".","3","1","4"],[".",".",".",".","2","7",".","5","."],["9","8",".",".",".",".",".","3","1"],[".","3","1","8",".","4",".",".","."],[".",".",".","1",".",".","8",".","5"],["7",".","6","2",".",".","1","8","."],[".","9",".","7",".",".",".",".","."],["4","1",".",".",".","5",".",".","7"]]
print(solve_sudoku(board))