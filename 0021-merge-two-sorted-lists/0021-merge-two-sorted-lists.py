class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def ListToSLL(l):
    if not l:  # 입력 리스트가 비어있는 경우 처리
        return None
    head = ListNode(l[0])
    curr = head
    for value in l[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    return head

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 이미 ListNode이기 때문에 ListToSLL 호출이 필요 없다면 삭제
        # list1 = ListToSLL(list1)
        # list2 = ListToSLL(list2)
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        # 남아있는 리스트 처리
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        return dummy.next
