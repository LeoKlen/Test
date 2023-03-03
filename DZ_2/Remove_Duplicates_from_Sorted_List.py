#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        if not head:
            return head
        head_now = head
        head_next = head.next
        ans=[]
        
        while head_next != None:
            if head_now.val == head_next.val:

                head_now.next = head_next.next
                head_next = head_next.next

            else:
                head_next = head_next.next
                head_now = head_now.next

        return head
