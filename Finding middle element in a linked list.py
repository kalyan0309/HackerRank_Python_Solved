class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        lst=[]
        c=0
        while head:
            lst.append(head.data)
            head = head.next
        return lst[len(lst)//2]
