class Queues:
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        if len(self.data) == 0:
            return True
        return False
# adds a new item to the rear of the queue
    def enqueue(self, value: any) -> any:
        self.data.insert(0, value)
# remove item from the list
    def dequeue(self) -> any:
        self.data.pop()

#Check first element
    def peek_elem(self):
        if not self.is_empty():
            return self.data[-1]
        return

que = Queues()
print(que.is_empty())
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
print(que.data)
print(que.is_empty())
que.dequeue()
que.dequeue()
print(que.data)

