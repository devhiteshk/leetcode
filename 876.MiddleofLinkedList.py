# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head):
        if head is None:
            return [0]
        else:
            count = 0
            temp = head
            while temp:
                count+=1
                temp = temp.next
                
            res = []
            i = 0
            mid = count//2
            
            temp1 = head
            while temp1:
                if i==mid:
                    return temp1
                temp1 = temp1.next
                i += 1