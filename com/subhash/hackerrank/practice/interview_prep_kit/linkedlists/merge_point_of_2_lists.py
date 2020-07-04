#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    head1, l1 = reverse_list(head1)
    # print_list(head1)
    # print(l1)
    # now head1 is at the end of common list
    # end is old head1

    head2, l2 = reverse_list(head2)
    # print_list(head2)
    # print(l2)
    # now head2 is old head1
    # end is old head2

    head1, l3 = reverse_list(head1)
    # print_list(head1)
    # print(l3)
    # now head1 is old head2
    # end is end of common list

    # b is length of uncommon list of old head2 (now head1)
    b = (l2 - l1 + l3) // 2
    # a is length of uncommon list of old head1 (now head2)
    a = l2 - b - 1

    trav = head2 if a < b else head1
    min_ab = min(a, b)
    for _ in range(min_ab):
        trav = trav.next

    return trav.data


def reverse_list(head):
    trav = head
    prev = None
    size = 0
    while trav:
        temp = trav.next
        trav.next = prev
        prev = trav
        trav = temp
        size += 1
    head = prev
    return head, size


def print_list(head):
    trav = head
    while trav:
        print(str(trav.data) + "->")
        trav = trav.next


if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = findMergeNode(llist1.head, llist2.head)

    print(str(result))
