# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

linklist = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        second = head
        while second is not None and second.next is not None:
            first = first.next
            second = second.next.next
        
        return first
    
ans = Solution.middleNode(Solution, linklist)
print(ans)