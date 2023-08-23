def ff(A,X,l=None,r=None):
    if l==None:
        l=0
    if r==None:
        r=len(A)-1
    if l==r:
        if A[l]==X:
            return True
    elif l<r:
        if A[l]+A[r]==X:
            return True
        elif A[l]+A[r]<X:
            return ff(A,X,l+1,r)
        else:
            return ff(A,X,l,r-1)

print(ff([1,2,3],4))
