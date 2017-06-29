"""
Implement a SinglyLinkedList object and a ListNode object, such that the
SinglyLinkedList object functions as a "container" for ListNode objects.

For the SinglyLinkedList object, it should have the following functions
implemented.

`.insert(element, N)` inserts element, a ListNode object, at position N. The
SinglyLinkedList object should now have one additional element.

`.delete(N)` deletes the element at position N. The SinglyLinkedList should now
have one fewer element.

`.append(element)` appends the element at the end of the SinglyLinkedList. The
SinglyLinkedList should now have one additional element.

`.pop(element)` takes the last element of the SinglyLinkedList, removes it from
the SinglyLinkedList, and returns it.

This question simultaneously tests object-oriented programming and algorithms.
"""


class SinglyLinkedList:
    def __init__(self, head):
        self.head = head

    def last_(self):
        curnode = self.head
        while curnode.next is not None:
            curnode = curnode.next
        return curnode

    def get_(self, N):
        """
        Gets the node at position N.
        """
        curnode = self.head
        i = 0
        while i < N:
            curnode = curnode.next

        return curnode

    def append(self, node):
        """
        Appends a node to the end of the SinglyLinkedList.
        """
        last_node = self.last_()
        last_node.next = node

    def delete(self, N):
        """
        Deletes the node at position N.
        """
        pre_node = self.get_(N-1)  # node before the one to be deleted.
        post_node = pre_node.next.next  # node after the one to be deleted.
        del pre_node.next
        pre_node.next = post_node

    def insert(self, element, N):
        pre_node = self.get_(N-1)  # node before the one to be deleted.
        post_node = pre_node.next  # the node at position N.
        pre_node.next = element
        element.next = post_node


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
