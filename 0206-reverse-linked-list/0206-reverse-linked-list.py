# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l, r = None, head
        
        while r:
            nextTemp = r.next
            r.next = l
            l = r
            r = nextTemp
        return l
        