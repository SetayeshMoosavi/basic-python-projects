import random
complist=[]
yourlist=[]
l=[]
b=[]
hint=[]
flag="false"
print("be bazi e fekre bekr khosh amadi \nsathe bazi e khod ra vared konid: 1=easy 2=hard:")
x=int(input(""))
if x==1:
    for j in range (4):
        complist.append((random.randint(1,4)))
    print("complist:  ",complist)
    for h in range (10):
        print(
            "shoma level e easy ra entekhab kardid \n 10 forsat darid ke 4 rang ra hads bezanid \nrang ha shamele:\nred=1 ,blue=2 ,yellow=3 ,green=4 \n")
        for i in range (4):
            y = int(input(" entekhab konid"))
            yourlist.append(y)
        print("yourlise:  " ,yourlist)

        for item in complist:
            l.append(item)
        print("L:  ",l)
        for n in range (4):
            if complist[n] == yourlist[n]:
                hint.append("black")
                b.append(complist[n])
                print("b:",b)
            else:
                for thing in b:
                    if thing in l:
                        l.remove((thing))
                        print("l jadid:",l)
                if yourlist[n] in (l ):
                    hint.append("white")
        print(hint)
        if hint==["black","black","black","black"]:
            flag="true"
            print("bordi!!!!!!!!!!")
        break
    if flag=="false":
        print("bakhti")
elif x==2:
    for j in range (5):
        complist.append((random.randint(1,5)))
    print("complist:  ",complist)
    for h in range (8):
        print(
            "shoma level e easy ra entekhab kardid \n 8 forsat darid ke 5 rang ra hads bezanid \nrang ha shamele:\nred=1 ,blue=2 ,yellow=3 ,green=4 , purple=5 \n")
        for i in range (5):
            y = int(input(" entekhab konid"))
            yourlist.append(y)
        print("yourlise:  " ,yourlist)

        for item in complist:
            l.append(item)
        print("L:  ",l)
        for n in range (5):
            if complist[n] == yourlist[n]:
                hint.append("black")
                b.append(complist[n])
                print("b:",b)
            else:
                for thing in b:
                    if thing in l:
                        l.remove((thing))
                        print("l jadid:",l)
                if yourlist[n] in (l ):
                    hint.append("white")
        print(hint)
        if hint==["black","black","black","black"]:
            flag="true"
            print("bordi!!!!!!!!!!")
        break
    if flag=="false":
        print("bakhti")
