"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if not head or not head.next:
        return 0

    s = set()
    trav = head
    while trav:
        if trav in s:
            return 1
        else:
            s.add(trav)
        trav = trav.next
    return 0