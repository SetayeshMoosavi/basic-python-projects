def place(l):
    x = 0
    y = 0
    l.split(",")
    for i in range(len(l)):
        if l[i].upper() == "R":
            x = x + 1
        elif l[i].upper() == "L":
            x = x - 1
        elif l[i].upper() == "U":
            y = y + 1
        elif l[i].upper() == "D":
            y = y - 1
    return(x,y)

l=input("")
print(place(l))