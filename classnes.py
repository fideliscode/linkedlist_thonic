class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_element = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_element

    def length(self):
        current_node = self.head
        # if current_node.data:
        count = 0
        while current_node.next != None:
            current_node = current_node.next
            count += 1
        return count

    def display(self):
        current_node = self.head
        elems = []
        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("index out of range!")
            return
        cur_node = self.head
        cur_index = 0
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index += 1

#mark the first none node and the following node,if indexed point to the next after the indexed
    def delete(self, index):
        if index >= self.length():
            print("index out of range!")
            return
        current_node = self.head
        current_index = 0
        while True:
            initialization_node = current_node
            current_node = initialization_node.next
            if current_index == index:
                initialization_node.next = current_node.next
                return
            current_index += 1
