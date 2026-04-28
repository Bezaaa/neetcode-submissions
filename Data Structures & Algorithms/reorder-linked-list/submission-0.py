# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """    
        1. divide the list in to 2
        2. reverse the second half
        3. merge them as we have 2 lists now
        """

        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
         # Step 2: Reverse the second half
        prev, curr = None, slow.next
        slow.next = None  
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # step 3
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            
        

            

        