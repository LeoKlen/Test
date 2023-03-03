#https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if  not head:
            return head
        current = head
        i = 1
        while current.next:
            i+=1
            current = current.next
        i = i // 2 
        current = head
        for  i in range(i):
            current = current.next
        return current
