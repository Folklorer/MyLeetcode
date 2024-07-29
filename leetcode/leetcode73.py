# 240729

def setZeroes(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    tmp = [[0]*m,[0]*n]
    for i in range(m):
        for j in range(n):
            if tmp[0][i] == 1 and tmp[1][j] == 1:
                continue
            if matrix[i][j] == 0:
                tmp[0][i] = 1
                tmp[1][j] = 1
    for i in range(m):
        for j in range(n):
            if tmp[0][i]==1 or tmp[1][j]==1:
                matrix[i][j] = 0
    return matrix

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroes(matrix))

