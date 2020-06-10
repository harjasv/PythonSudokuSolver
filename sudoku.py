import time

print("Sudoku!")

#grid is #91 in the book
sudoku=[[9, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 1],
        [3, 0, 0, 0, 0, 0, 7, 9, 8],
        [0, 0, 8, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 6, 0],
        [1, 0, 6, 0, 0, 9, 0, 4, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [8, 4, 0, 0, 3, 1, 0, 2, 0],
        [0, 3, 0, 0, 4, 0, 0, 0, 0]]

def print_sudoku(s):
    for x in range(len(s)):
        if(x % 3 == 0 and x != 0):
            print("---------------------")
        for y in range(len(s[x])):
            if(y == 8):
                print(s[x][y])
            else:
                if(y % 3 == 0 and y != 0):
                    print("|"),
                print(s[x][y]),

def check_valid(n, x, y, s):

    #check row
    for i in range(len(s[x])):
        if(s[x][i] == n):
            return False

    #check column
    for j in range(len(s)):
        if(s[j][y] == n):
            return False

    #check box
    box_x = x // 3
    box_y = y // 3

    for k in range(box_x*3, (box_x*3 + 3)):
        for l in range(box_y*3, (box_y*3 + 3)):
            if(s[k][l] == n):
                return False

    return True

def is_full(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(s[i][j] == 0):
                return False
    return True

def find_empty(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(s[i][j] == 0):
                return (i, j)

    return None

#Backtracking algorithm
def backtrack(s):
    find = find_empty(s)

    if(find):
        a, b = find
    else:
        return True

    for i in range(1, 10):
        if(check_valid(i, a, b, s)):
            s[a][b] = i
            if(backtrack(s)):
                return True
    s[a][b] = 0

print_sudoku(sudoku)
print("\n")
print("Solution:")
tic = time.time()
backtrack(sudoku)
toc = time.time()
print_sudoku(sudoku)
if(is_full(sudoku)):
    print("Done - ")
    print(toc - tic)
else:
    print("Error")
