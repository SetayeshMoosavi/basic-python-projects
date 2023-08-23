def max_min(mylist):

    if len(mylist) == 1 or len(mylist) == 0 :
        return (mylist[0],mylist[0])
    else:
        return( min(mylist[0], max_min(mylist[1:])[0]),max(mylist[0], max_min(mylist[1:])[1]))
l=input("please enter your list and seperate them with space: ").split(" ")
print (max_min(l))