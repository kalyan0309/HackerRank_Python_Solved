def reversePrint(llist):
    # Write your code here
    l = []
    while llist:
        l.append(llist.data)
        llist = llist.next
    l = l[::-1]
    for i in l:
        print(i)
