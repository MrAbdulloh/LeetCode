# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if not head:
            return head

        current = head
        while current and current.next:
            g = gcd(current.val, current.next.val)
            new_node = ListNode(g)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        return head
