class Stack(object):
    def __init__(self):
        self.stack = []

    # Push is a bottleneck.
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.isEmpty():
            return self.stack.remove(self.stack[-1])

    def top(self):
        if not self.isEmpty():
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def __str__(self):
        result = "["
        for num in self.stack:
            result += str(num) + " "
        result += "\b]"
        return result
