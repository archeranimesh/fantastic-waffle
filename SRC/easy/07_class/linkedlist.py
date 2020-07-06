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
