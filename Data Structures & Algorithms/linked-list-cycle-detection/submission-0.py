# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        current = head
        while current and current.next:
            if current.val in visited:
                return True
            visited.append(current.val)
            current = current.next
        return False
        