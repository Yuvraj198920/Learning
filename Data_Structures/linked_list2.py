class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LnkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        # Loop through linked list to reach at the end
        while cur.next != None:
            cur = cur.next

        # Now you are at the end of list append your new node
        cur.next = new_node
    
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total+=1
            cur = cur.next
            
        return total
    
    def display(self):
        cur = self.head
        elem = []
        while cur.next != None:
            elem.append(cur.data)
            cur = cur.next

        return elem
    
linkedList = LnkedList()
linkedList.append(1)
linkedList.append(2)

print(linkedList.display())
print(linkedList.length())