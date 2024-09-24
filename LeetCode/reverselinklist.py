# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

h1 = ListNode(1,ListNode(2))
h2 = ListNode()

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        bufflist = []

        while head:
            bufflist.append(head.val)
            head = head.next

        dummy = ListNode()
        cur = dummy

        while len(bufflist) > 0:
            cur.next = ListNode(bufflist.pop())
            cur = cur.next

        if dummy.next:
            return dummy.next
        else:
            return None
    
ans = Solution.reverseList(Solution, h1)
ans2 = Solution.reverseList(Solution, h2)

print(ans, ans2)