def isfeasible(board,row,col):
    for i in range(row):
        if board[i][col]==1:
            return False
        if row-i-1>=0 and col-i-1>=0:
            if board[row-i-1][col-i-1]==1:
                return False
        if row-i-1>=0 and col+i+1<n:
            if board[row-i-1][col+i+1]==1:
                return False
    if row-1>=0 and col+2<n:
        if board[row-1][col+2]==1:
            return False
    if row-1>=0 and col-2<n:
        if board[row-1][col-2]==1:
            return False
    if row-2>=0 and col-1<n:
        if board[row-2][col-1]==1:
            return False
    if row-2>=0 and col+1<n:
        if board[row-2][col+1]==1:
            return False
    return True

def soleNqueens(board,row):
    if  row>=n:
        return True
    for j in range(n):
        if isfeasible(board,row,j):
            board[row][j]=1
            if soleNqueens(board,row+1):
                return True
            board[row][j]=0
    return False

board=[[0,0],[0,0]]
n=2
while soleNqueens(board,0) is False:
    n+=1
    board=[]
    for i in range (n):
        board.append( [0]*n)

for item in board:
    print(item)

print("the suitable n is: ",n)


