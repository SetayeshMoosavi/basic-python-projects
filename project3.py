def isprime(n):
    h=0
    if n == 1 or n == 0:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                h = h + 1
        if h > 0:
            return False
        else:
            return True

def rastprime(n):
    for i in range(len(str(n))):
        if isprime(n):
            n = n // 10
        else:
            return False
    return True

def reverse(n):
    x=[]
    a=0
    x = list(str(n))
    x.reverse()
    a=int(float(''.join(x)))
    return(a)

def chapprime(n):
    a = reverse(n)
    for i in range(len(str(n))):
        if rastprime(reverse(a)):
            a = a // 10
        else:
            return False
    return True


def kotahshodegi(n):
    if rastprime(n) and chapprime(n):
        return True
    else:
        return False

n=int(input("adade khod ra vared namaeed:  "))
r=[]
for i in range(n):
    if kotahshodegi(i):
        r.append(i)
print(r)
