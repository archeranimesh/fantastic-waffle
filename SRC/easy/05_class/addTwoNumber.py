# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_number = []
        l2_number = []
        while l1 is not None:
            l1_number.append(l1.val)
            l1 = l1.next

        while l2 is not None:
            l2_number.append(l2.val)
            l2 = l2.next
        l1_number = int("".join(str(i) for i in l1_number)[::-1], 10)
        l2_number = int("".join(str(i) for i in l2_number)[::-1], 10)
        number = l2_number + l1_number
        list_number = str(number)[::-1]
        hello = [int(x) for x in list_number]
        # https://www.codesdope.com/blog/article/inserting-a-new-node-in-a-linked-list-in-c/
        head = None
        for x in hello:
            current = ListNode(x)
            if head is None:
                head = current
            else:
                prev.next = current
            prev = current
        return head
