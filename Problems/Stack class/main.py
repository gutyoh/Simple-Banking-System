class Stack():

    def __init__(self):
        self.items = []
        pass

    def push(self, el):
        self.items.append(el)
        pass

    def pop(self):
        return self.items.pop()
        pass

    def peek(self):
        return self.items[len(self.items)-1]
        pass

    def is_empty(self):
        return self.items == []
        pass