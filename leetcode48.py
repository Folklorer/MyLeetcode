# 240726

# poor TIME!!
def rotate(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(m): 
        matrix[i] = matrix[i][::-1]
    return matrix

# m[i][j] -> m[j][-i]
def rotate2(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    tmp_mat = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            tmp_mat[j][-i] = matrix[i][j]
    matrix[:] = tmp_mat
    return matrix

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(rotate(mat))