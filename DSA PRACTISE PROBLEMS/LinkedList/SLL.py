

# All the operations are done on linkedlist assuming that its not empty and and has more than 1 node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Sll:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        new_node = Node()
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert(self, value, index):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            elif index == -1:
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                for _ in range(index-1):
                    temp_node = temp_node.next
                next_node = temp_node.next
                new_node.next = next_node
                temp_node.next = new_node

    def traversal(self):
        current = self.head
        while current is not None:
            print(current.vaule)
            current = current.next

    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False

    def search2(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1

    def update(self, value, index):
        if index == 0:
            self.head.value = value
        elif index == -1:
            self.tail.value = value
            # temp_node = self.head
            # while temp_node.next is not None:
            #     temp_node = temp_node.next
            # temp_node.value = value
        else:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            temp_node.value = value

    def remove(self,index):
        if index == 0:
            self.head = self.head.next
        elif index == -1:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            temp_node.next = None
            self.tail = temp_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            next_node = temp_node.next
            temp_node.next = next_node.next
            next_node.next = None






sll1 = Sll()
sll1.append(0)
sll1.append(1)
sll1.append(2)
sll1.append(3)
sll1.append(4)
sll1.append(5)
# sll1.insert(9, 0)
# sll1.insert(9, -1)
# sll1.insert(9, 3)
# sll1.update(0,0)
# sll1.update(6,-1)
sll1.remove(0)
sll1.remove(-1)
sll1.remove(2)
print(sll1)

