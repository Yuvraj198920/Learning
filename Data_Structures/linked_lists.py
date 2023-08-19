class Node:
    def __init__(self, name, number) -> None:
        self.name = name
        self.number = number
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def add_contact(self, name, number):
        new_contact = Node(name, number)
        if self.head is None:
            self.head = new_contact

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_contact
        print("Contact added successfully")

    def display_contacts(self):
        current = self.head
        if current is None:
            print("Contact list is empty")
        else:
            print("Contact list: ")
            while current:
                print(f"Name: {current.name}, Phone: {current.number}")
                current = current.next


contact_list = LinkedList()
contact_list.add_contact("Yuvraj", "7028555029")
contact_list.add_contact("Yuvraj_singapore", "84698214")
contact_list.add_contact("Suraj", "123343432")
contact_list.display_contacts()