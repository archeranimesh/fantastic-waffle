# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        number = []
        while head is not None:
            number.append(head.val)
            head = head.next
        return number == number[::-1]
