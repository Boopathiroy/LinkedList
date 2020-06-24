
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    """Appending the element to the end of the list"""
    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    """Printing the linkedlist"""
    def print_lis(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    """Adding the element to the front of the linked List"""
    def prepend(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    """Insering Node after specific Node"""
    def insert_after_node(self,prev_node,data):
        if not prev_node:
            print("The previous node is not in this list")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    """Node Deletion at the end of the list"""
    def delete_node(self,key):
        cur_node = self.head
        if cur_node and cur_node == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node!=key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    """Deleting Node at position"""
    def delete_node_at_pos(self,pos):
        cur_node = self.head
        if cur_node and cur_node == pos:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count= 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count+=1
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count+=1
            cur_node = cur_node.next
        return count

    def len_recursive(self,node):
        if node is None:
            return 0
        return 1+ self.len_iterative(node.next)

llist = LinkedList()
llist.append('B')
llist.append('o')
llist.append('p')
llist.prepend('t')
llist.insert_after_node(llist.head.next,'o')
llist.print_lis()
llist.delete_node("t")
print(llist.len_iterative())
llist.delete_node_at_pos(3)
llist.print_lis()



