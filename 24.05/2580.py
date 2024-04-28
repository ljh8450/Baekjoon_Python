def is_valid(x, y, num, grid):
    # 같은 행에 같은 숫자가 있는지 확인
    for i in range(9):
        if grid[x][i] == num:
            return False
    # 같은 열에 같은 숫자가 있는지 확인
    for i in range(9):
        if grid[i][y] == num:
            return False
    # 3x3 서브그리드에 같은 숫자가 있는지 확인
    start_row = (x // 3) * 3
    start_col = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(grid):
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:  # 빈 칸 찾기
                for num in range(1, 10):  # 1부터 9까지의 숫자 시도
                    if is_valid(x, y, num, grid):
                        grid[x][y] = num
                        if solve_sudoku(grid):
                            return True
                        grid[x][y] = 0
                return False
    return True

# 스도쿠 보드 입력
sudoku = [
    [0, 3, 5, 4, 6, 9, 2, 7, 8],
    [7, 8, 2, 1, 0, 5, 6, 0, 9],
    [0, 6, 0, 2, 7, 8, 1, 3, 5],
    [3, 2, 1, 0, 4, 6, 8, 9, 7],
    [8, 0, 4, 9, 1, 3, 5, 0, 6],
    [5, 9, 6, 8, 2, 0, 4, 1, 3],
    [9, 1, 7, 6, 5, 2, 0, 8, 0],
    [6, 0, 3, 7, 0, 1, 9, 5, 2],
    [2, 5, 8, 3, 9, 4, 7, 6, 0]
]

if solve_sudoku(sudoku):
    for row in sudoku:
        print(" ".join(map(str, row)))
else:
    print("No solution exists")