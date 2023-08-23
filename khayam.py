n=3
l=[]
for j in range(n):
    for i in range(j+2):
        l.append([1]*(j+1))
        if j>1:
            for k in range(1,j):
                l[j][k]= l[j][k]+l[j-1][k-1]+l[j-1][k]
                print(l[j])

        else:
            print(l[j])