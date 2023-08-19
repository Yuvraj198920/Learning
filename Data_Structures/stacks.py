
class Stack:
    def __init__(self):
        self.arr = []

    def is_empty(self) ->bool:
        if len(self.arr) == 0:
            return True
        return False

    def push(self, elem: any) -> None:
        self.arr.append(elem)

    def pop(self) -> any:
        self.arr.pop()
        return self.arr

stack= Stack()
print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.arr)
stack.pop()
print(stack.arr)

