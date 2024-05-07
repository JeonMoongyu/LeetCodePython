# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA = set()
        currA, currB = headA, headB
        while currA:
            setA.add(currA)
            currA = currA.next
        while currB:
            if currB in setA:
                return currB
            currB = currB.next
        return None