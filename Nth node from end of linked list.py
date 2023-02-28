#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    #code here
    lst=[]
    while head:
        lst.append(head.data)
        head = head.next
    lst = lst[::-1]
    for i in range(len(lst)):
        if i == n-1:
            return lst[i]
    return -1
