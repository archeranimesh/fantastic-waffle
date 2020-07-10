# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow_p = head
        fast_p = head
        for i in range(n):
            if fast_p.next == None:
                if i == n - 1:
                    head = head.next
                return head
            fast_p = fast_p.next

        while fast_p.next is not None:
            slow_p = slow_p.next
            fast_p = fast_p.next
            # print(slow_p.val, fast_p.val, end=" ")
        slow_p.next = slow_p.next.next
        return head


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    soln = Solution()
    soln.removeNthFromEnd(n1, 2)
    temp = n1
    while temp:
        print(temp.val)
        temp = temp.next
