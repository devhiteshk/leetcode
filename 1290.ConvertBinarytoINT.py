# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
        res = "0b"
        if head is None:
            return 0
        else:
            temp = head
            while temp:
                res += str(temp.val)
                temp = temp.next
        return int(res,2)