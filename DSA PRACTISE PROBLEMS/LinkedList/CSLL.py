class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Csll:
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
            result += '->'
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self, value, index):
        if index > self. length:
            raise Exception("index out of range")
        new_node = Node(value)
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == -1 or index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            next_node = temp_node.next
            new_node.next = next_node
            temp_node.next = new_node
        self.length += 1

    def traversal(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            if current == self.head:
                break

    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get_index(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break
        return -1

    def update(self, value, index):
        if index == 0:
            self.head.value = value
        elif index == -1 or index == self.length:
            self.tail.value = value
        else:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            temp_node.value = value

    def remove(self, index):
        if index == 0:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        elif index == -1 or index == self.length:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next

            temp_node.next = self.head
            self.tail = temp_node

        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            next_node = temp_node.next
            temp_node.next = next_node.next
            next_node.next = None

    def delete_all(self):
        self.tail.next = None
        self.head = None
        self.tail = None


csll1 = Csll()
csll1.append(0)
csll1.append(1)
csll1.append(2)
csll1.append(3)
csll1.insert(10, 0)
csll1.insert(10, -1)
print(csll1)
