## Remove Dups: Write code to remove duplicates from an unsorted linked list.
#
#class Node:
#    def __init__(self, data, next):
#        self.data = data
#        self.next = Node(None,None)
#
#    def appendToTail(self):
#        end = Node(self.data)
#        n = self
#        while (n.next is not None):
#            n = n.next
#        n.next = end
#
#    def __str__(self):
#        return ("Node Data: " + str(self.data) + " Next: " + str(self.next))
#
#
#def deleteNode(head, d):
#    n = head
#
#    if (n.data == d):
#        return head.next # moved head #
#
#    while (n.next is not None):
#        if (n.next.data == d):
#            n.next = n.next.next
#            return head # head didn't change #
#        n = n.next
#    return head
#

class node:
    def __init__(self):
        self.data = None
        self.next = None


class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = node()
        new_node.data = data
        new_node.next = self.cur_node
        self.cur_node = new_node

    def list_print(self):
        node = self.cur_node
        while node:
            print node.data
            node = node.next

ll = linked_list()

for num in range(1,11):
   ll.add_node(num)


# Write code to remove duplicates from an unsorted linked list

unsorted = linked_list()
unsorted.add_node(7)
unsorted.add_node(6)
unsorted.add_node(4)
unsorted.add_node(7)
unsorted.add_node(2)
unsorted.add_node(1)

unsorted.list_print()

deleteDupes(list):
    for item in list:
        buff = item
        if item.next ==

