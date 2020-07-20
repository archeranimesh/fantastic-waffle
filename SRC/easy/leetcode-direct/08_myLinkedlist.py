class MyLinkedList:
    def __init__(self, val, next=None):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.next = next

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        i = 0
        node = self
        while node and i < index:
            node = node.next
            i += 1
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.val is None:
            self.val = val
        else:
            new_node = MyLinkedList()
            new_node.val = self.val
            new_node.next = self.next
            self.val = val
            self.next = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.val is None:
            self.val = val
        else:
            node = self
            while node.next:
                node = node.next
            node.next = MyLinkedList()
            node.next.val = val

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return

        i = 0
        curr_node = self
        while i < index - 1 and curr_node.next:
            curr_node = curr_node.next
            i += 1

        if curr_node.next is None and i < index - 1:
            return

        new_node = MyLinkedList()
        new_node.val = val
        new_node.next = curr_node.next
        curr_node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            if self.next:
                self.val = self.next.val
                self.next = self.next.next
        else:
            i = 0
            curr_node = self
            while i < index - 1 and curr_node.next:
                curr_node = curr_node.next
                i += 1
            if curr_node.next is None and i < index - 1:
                return
            if curr_node.next:
                curr_node.next = curr_node.next.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(index)
obj.addAtHead(val)
obj.addAtTail(val)
obj.addAtIndex(index, val)
obj.deleteAtIndex(index)
