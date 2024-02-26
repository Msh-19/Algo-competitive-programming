# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        currB = headB
        nodesB = set()

                
        while currB:
            nodesB.add(currB)
            currB = currB.next

        while currA:
            if currA in nodesB:
                return currA
            currA = currA.next

        return None