# 240725

def isValidSudoku(board: list[list[str]]) -> bool:
    def Valid(lst):
        lst = [i for i in lst if i != "."]
        return len(lst)==len(set(lst))
    colboard = [[] for i in range(9)]
    squborad = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            colboard[i].append(board[j][i])
            if i<3:
                squborad[i//3+j//3].append(board[i][j]) 
            elif i<6 and i>2:
                squborad[i//3+j//3+2].append(board[i][j])
            else:
                squborad[i//3+j//3+4].append(board[i][j])
    for i in range(9):
        if Valid(board[i]) == False:
            return False
        elif Valid(colboard[i]) == False:
            return False
        elif Valid(squborad[i]) == False:
            return False
    return True
