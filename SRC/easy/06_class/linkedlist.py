class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList(object):
    def __init__(self, Node):
        self.head = Node

    # Insert Node at the front.
    def push(self, val):
        # Allocate the new node
        new_node = Node(val)
        # Point the new node's next to head
        new_node.next = self.head
        # modify the head
        self.head = new_node

    # Insert Node at the end
    def append(self, val):
        new_node = Node(4)

        # Linked List is empty
        if self.head is None:
            self.head = new_node

        # traverse the list
        last = self.head
        while last.next is not None:
            last = last.next

        last.next = new_node

    def insertAfterIndex(self, index, value):
        if index < 0:
            return
        # create new node
        new_node = Node(value)
        prev = None
        curr = self.head
        for _i in range(index + 1):
            prev = curr
            curr = curr.next
        if prev:
            prev.next = new_node
            new_node.next = curr

    def insertAfterValue(self, value_after, value):
        curr = self.head

        while curr is not None:
            if curr.value == value_after:
                break
            curr = curr.next
        else:
            return
        new_node = Node(value)
        new_node.next = curr.next
        curr.next = new_node

    def deleteNode(self, key):
        temp = self.head

        if temp is not None:
            if temp.value == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.value == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

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
    linkedList.push(0)
    print(str(linkedList))
    linkedList.append(4)
    print(str(linkedList))
    linkedList.insertAfterIndex(2, 2.5)
    print(str(linkedList))
    linkedList.insertAfterIndex(1, 1.5)
    print(str(linkedList))
    linkedList.insertAfterIndex(-1, 0.5)
    print(str(linkedList))
    linkedList.insertAfterIndex(6, 4.5)
    print(str(linkedList))
    linkedList.insertAfterValue(1.5, 1.75)
    print(str(linkedList))
    linkedList.insertAfterValue(0, 0.25)
    print(str(linkedList))
    linkedList.deleteNode(100)
    print(str(linkedList))
    # linkedList = LinkedList(None)
    # print(str(linkedList))
    # linkedList.insertAfterValue(0, 0.25)
    # print(str(linkedList))
