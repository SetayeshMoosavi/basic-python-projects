def ischarkhesh(n):

    l=[]
    count=0
    charkheshlist=[]
    b=n
    while b!=0:
        a=b//10
        c=b%10
        l.append(c)
        b=a
        count=count+1

    def charkhesh(n):
        for j in range(count):
            a=n//((10)**(count-1))
            b=n%((10)**(count-1))
            y=(b*10)+a
            charkheshlist.append(y)
            n=y
        return (charkheshlist)

    def isprime(n):
        h = 0
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

    o=0
    for j in range (count):
        if isprime(charkhesh(n)[j]):
            o=o+1
    if o==count:
        return True

x=int(input("adad ra vared konid:  "))
r = []
for n in range(2,x):
    if ischarkhesh(n):
        r.append(n)
print(r)