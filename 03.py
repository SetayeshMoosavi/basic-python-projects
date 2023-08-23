def ff(A,X,l=None,r=None):
    x=X/2
    if l==None:
        l=0
    if r==None:
        r= len(A)-1
    if l==r:
        if A[l]<=x:
            return l
        else:
            return l-1
    elif l<r:
        mid=int((l+r)/2)
        if A[mid]==x:
            return mid
        elif A[mid]>x:
            return ff(A,X,l,mid)
        else:
            return ff(A,X,mid+1,r)
def fff(A,X ):
    result=[]
    a=(ff(A,X))
    a1=A[0:a+1]
    a2=A[a+1:]
    for item in a1:
        for iitem in a2:
            if item+iitem==X:
                result.append([item,iitem])
    return result
A = [1,2,3,4,5]
X =7
print(fff(A, X))
