class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        elif not self.head.next:
            self.head.next = new_node
            return
        
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node


    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current_node = self.head

        self.head = new_node

        self.head.next = current_node


    def insert(self, data):
        new_node = Node(data)

        # Scenario 1 - Linked list is empty.
        if not self.head:
            self.head = new_node
            return

        current_node = self.head

        # Scenario 2 - Prepend to linked list.
        if data < self.head.data:
            self.head = new_node
            self.head.next = current_node
            return

        # Traverse list
        prev_node = None

        while current_node.next is not None and current_node.data < data:
            prev_node = current_node
            current_node = current_node.next

        # Scenario 3 - Insert in middle of list
        if current_node.data > data:
            prev_node.next = new_node
            new_node.next = current_node

        # Scenario 4 - Append to list
        else:
            current_node.next = new_node


    def display(self):
        current_node = self.head

        if not self.head:
            print('Linked list is empty.')
            return
        
        while current_node.next is not None:
            print(f"'{current_node.data}'", end=" -> ")
            current_node = current_node.next

        print(f"'{current_node.data}'")


# ==== Main program ====
test = LinkedList()

test.insert('James')
test.insert('Antoine')
test.insert('Bailey')
test.insert('Charlie')
test.insert('Levi')
test.insert('Tom')
test.display()
