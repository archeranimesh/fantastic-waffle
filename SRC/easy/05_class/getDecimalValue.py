# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        number = []
        while temp is not None:
            number.append(temp.val)
            temp = temp.next
        # https://www.tutorialspoint.com/binary-list-to-integer-in-python
        result = int("".join(str(i) for i in number), 2)
        return result


if __name__ == "__main__":
    solution = Solution()
