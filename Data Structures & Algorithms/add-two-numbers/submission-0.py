# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
     
        result_head = None
        result_tail = None
        carry = 0

        while l1 or l2:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            new_node = ListNode(total % 10)
            carry = total // 10

            if not result_head:
                result_head = result_tail = new_node
            else:
                result_tail.next = new_node
                result_tail = result_tail.next

        if carry > 0:
            result_tail.next = ListNode(carry)

        return result_head
        
        