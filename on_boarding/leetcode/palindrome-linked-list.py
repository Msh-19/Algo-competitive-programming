# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow

        while curr:
            nxt =curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        firstHalf, reversedHalf = head, prev

        while firstHalf and reversedHalf:
            if firstHalf.val != reversedHalf.val:
                return False

            firstHalf = firstHalf.next
            reversedHalf =  reversedHalf.next

        return True