def max_min(mylist):
    def minn(mylist):
        if len(mylist) == 1:
            return mylist[0]
        else:
            return min(mylist[0], min(mylist[1:]))
    def maxx(mylist):
        if len(mylist) == 1:
            return mylist[0]
        else:
            return max(mylist[0], max(mylist[1:]))
    print("min:",minn(mylist))
    print("max:",maxx(mylist))

l=input("please enter your list and seperate them with space: ").split(" ")
max_min(l)