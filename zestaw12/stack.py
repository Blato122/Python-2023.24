class Stack:
    def __init__(self, capacity=10):
        self.storage = capacity * [None]
        self.size = 0
        self.capacity = capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def push(self, data):
        if self.is_full():
            raise IndexError("trying to push to a full stack")
        self.storage[self.size] = data
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("trying to pop from an empty stack")
        self.size -= 1
        data = self.storage[self.size]
        self.storage[self.size] = None
        return data

if __name__ == "__main__":
    s = Stack()
    s.pop()