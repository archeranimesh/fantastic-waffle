class Node(object):
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList(object):
    def __init__(self, head: Node):
        self.head = head

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next

    def nth_element_from_last(self, n) -> int:
        first = second = self.head

        while n > 0:
            n -= 1
            second = second.next
        while second is not None:
            first = first.next
            second = second.next
        return first.val


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    # connect the nodes
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    linked_list = LinkedList(n1)
    linked_list.print_list()
    print()
    print(linked_list.nth_element_from_last(2))
