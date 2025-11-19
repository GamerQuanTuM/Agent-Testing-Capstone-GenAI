"""
Reverse Linked List (iterative)
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def list_from_pylist(vals):
    head = None
    tail = None
    for v in vals:
        node = ListNode(v)
        if not head:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def pylist_from_list(head: Optional[ListNode]):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == '__main__':
    head = list_from_pylist([1, 2, 3, 4, 5])
    rev = reverse_list(head)
    print('reverse_list:', pylist_from_list(rev))  # expected [5,4,3,2,1]
