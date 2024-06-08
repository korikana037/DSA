class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Cdll:
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
            if temp_node == self.head:
                break
            result += '<=>'
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.head.prev = new_node
            self.tail.next = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
                new_node.prev = new_node
            else:
                self.head.prev = new_node
                self.tail.next = new_node
                new_node.next = self.head
                new_node.prev = self.tail
                self.head = new_node
        elif index == -1 or index == self.length:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
                new_node.prev = new_node
            else:
                self.tail.next = new_node
                self.head.prev = new_node
                new_node.prev = self.tail
                new_node.next = self.head
                self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            next_node = temp_node.next
            temp_node.next = new_node
            new_node.prev = temp_node
            next_node.prev = new_node
            new_node.next = next_node
        self.length += 1

    def traversal(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            if current == self.head:
                break

    def reverse_traversal(self):
        current = self.tail
        while current is not None:
            print(current.value)
            current = current.prev
            if current == self.tail:
                break

    def search(self, target):
        current = self.head
        while current is not None:
            if current == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get_index(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break
        return -1

    def get_value(self, index):
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

    def remove(self, index,):
        if index == 0:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                removing_node = self.head
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
                removing_node.next = None
                removing_node.prev = None
        elif index == -1 or index == self.length:
            removing_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            removing_node.next = None
            removing_node.prev = None

        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            next_node = temp_node.next
            temp_node.next = next_node.next
            next_node.next.prev = temp_node
            temp_node.next = None
            temp_node.prev = None
        self.length -= 1

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
