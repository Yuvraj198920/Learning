class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class LnkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        # Loop through linked list to reach at the end
        while cur.next != None:
            cur = cur.next

            # Now you are at the end of list append your new node
        cur.next = new_node
