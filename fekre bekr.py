import random
def tabdil(L):
    x=[]
    for i in range(n):
        if L[i]=="yellow":
            x.append(1)
        if L[i]=="red":
            x.append(2)
        if L[i]=="blue":
            x.append(3)
        if L[i]=="green":
            x.append(4)
        if L[i]=="pink":
            x.append(5)
        if L[i]=="orange":
            x.append(6)
    return(x)
color=["yellow","red","blue","green","pink","orange"]
n=int(input("lotfa tedad rang ra vared konid(<7):"))
if n>6:
   print("tedad rang namotabar ast")
   exit()
f=int(input("lotfa tedad forsat ra moshakhas konid:"))
listcolor=[]
for i in range(n):
    listcolor.append(color[i])
print(listcolor)
cpu=[]
for i in range(n):
    cpu.append(random.randint(1,n))
for i in range(f):
    black=0
    white=0
    c=[]
    for i in range(n):
        c.append(cpu[i])
    user=(input("range mored nazar ra ba space vared konid:")).split(" ")
    if len(user)!=n:
        print("tedad rang vared shode eshtebah ast")
        exit()
    b=tabdil(user)
    for i in range(n):
        if b[i]==c[i]:
           c[i]="g"
           black=black+1
    for i in range(n):
        for j in range(n):
            if c[i]==b[j]:
               c[i]="k"
               white=white+1
    if black==n:
       print("you won")
       exit()
    else:
        print("black:"+str(black))
        print("white:"+str(white))
listcpu=[]
for item in cpu:
    listcpu.append(color[item-1])
print("you lost")
print(listcpu)