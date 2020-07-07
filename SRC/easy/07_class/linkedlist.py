class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList(object):
    def __init__(self, Node):
        self.head = Node

    def reverse_loop(self):
        prev = None
        curr = self.head
        next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def reverse_recursive(self, head):
        # Base Condition
        if head is None or head.next is None:
            return head

        print(head.value)
        rest = self.reverse_recursive(head.next)

        head.next.next = head
        head.next = None

        return rest

    #  Floyd’s Cycle-Finding Algorithm
    def detect_loop(self):
        slow_p = self.head
        fast_p = self.head

        while slow_p and fast_p and fast_p.next:
            fast_p = fast_p.next.next
            slow_p = slow_p.next
            if slow_p == fast_p:
                return (True, slow_p.value)

    # use set to detect loop
    def detect_loop_set(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return (True, temp.value)
            s.add(temp)
            temp = temp.next
        return (False, None)

    # https://stackoverflow.com/questions/28269643/python-unordered-listwith-nodes-str-method
    def __str__(self):
        temp = self.head
        result = "["
        if temp != None:
            result += " " + str(temp.value) + " -> "
            temp = temp.next
        while temp:
            result += " " + str(temp.value)
            temp = temp.next
            if temp:
                result += " -> "
            else:
                result += " -> NULL"
        result += " ]"
        return result


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    n3 = Node(3)
    n2.next = n3
    linkedList = LinkedList(n1)
    print(str(linkedList))
    linkedList.reverse_loop()
    print(str(linkedList))
    # Reverse a Empty List
    linkedList = LinkedList(None)
    print(str(linkedList))
    linkedList.reverse_loop()
    print(str(linkedList))
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    n3 = Node(3)
    n2.next = n3
    linkedList = LinkedList(n1)
    print(str(linkedList))
    linkedList.head = linkedList.reverse_recursive(linkedList.head)
    print(str(linkedList))
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n4
    linkedList = LinkedList(n1)
    # print(linkedList.detect_loop())
    print(linkedList.detect_loop_set())
# 34:00
