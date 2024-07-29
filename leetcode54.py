# 240726

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    m, n = len(matrix), len(matrix[0])
    ans = []
    round = 0
    if m == 1:
        return matrix[0]
    if n == 1:
        return [matrix[i][0] for i in range(len(matrix))]
    def trival(ans,m,n,round):
        print("ans: ", ans)
        for j in range(round,n-1-round):
            ans.append(matrix[round][j])
        for i in range(round,m-1-round):
            ans.append(matrix[i][n-1-round])
        for k in range(n-1-round,round,-1):
            ans.append(matrix[m-1-round][k])
        for m in range(m-1-round,round,-1):
            ans.append(matrix[m][round])
        return
    while round <= n-1-round and round <= m-1-round:
        trival(ans,m,n,round)
        if round == n-1-round and round == m-1-round:
            ans.append(matrix[round][round])
        round += 1
    return ans[:m*n]

# mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# mat = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# mat = [[1],[2],[3]]
# mat = [[1,2,3]]
mat = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
print(spiralOrder(mat))        
