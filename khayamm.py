def khayam(i):
    if i==1:
        l=[1]
    else:
        khayamprime=khayam(i-1)
        l=[1]
        for j in range (i-2):
            l.append(khayamprime[j]+khayamprime[j+1])
        l.append(1)

    return(l)
n=int(input("enter n"))
for i in range(1,n+1):
    print(khayam(i))