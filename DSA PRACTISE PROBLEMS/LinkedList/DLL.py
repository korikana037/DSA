class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Dll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node.next is not None:
                result += '<=>'
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        elif index == -1 or index == self.length:
            self.tail.next = new_node
            new_node.next = self.tail
            self.tail = new_node

        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            next_node = temp_node.next
            new_node.next = next_node
            new_node.prev = temp_node
            temp_node.next = new_node
            next_node.prev = new_node
        self.length += 1

    def traversal(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def reverse_traversal(self):
        current = self.tail
        while current is not None:
            print(current.value)
            current = current.prev

    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False

    def get_index(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1

    def get_value(self, index):
        if index == 0:
            return self.head.value
        elif index == -1 or index == self.length:
            return self.tail.value
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.value

    def update(self, index, value):
        if index == 0:
            self.head.value = value
        elif index == -1 or index == self.length:
            self.tail.value = value
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.value = value

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == -1 or index == self.length:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            next_node = temp_node.next
            temp_node.next = next_node.next
            next_node.next.prev = temp_node
        self.length -= 1

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
