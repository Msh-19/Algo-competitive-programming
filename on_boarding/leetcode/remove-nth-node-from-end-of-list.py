# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = start = ListNode(0, head)
        k = 0

        while k <= n:
            fast = fast.next
            k += 1

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return start.next