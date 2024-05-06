# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = self.SLLtoList(head)
        arr = arr[::-1]
        return self.ListtoSLL(arr)
    def SLLtoList(self, head):
        out = []
        while head:
            out.append(head.val)
            head = head.next
        return out
    def ListtoSLL(self, arr):
        if arr == []:
            return None
        out = curr = ListNode(arr[0])
        for i in range(1, len(arr)):
            new = ListNode(arr[i])
            curr.next = new
            curr = new
        return out