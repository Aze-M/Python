from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        

    if l1 is not None:
        l1num = []

        while l1 != None:
            l1num.insert(0,str(l1.val))
            l1 = l1.next

    if l2 is not None:
        l2num = []

        while l2 != None:
            l2num.insert(0,str(l2.val))
            l2 = l2.next

    l1num = int(''.join(l1num))
    l2num = int(''.join(l2num))

    try:
        result = str(l1num + l2num)
    except TypeError and ValueError:
        pass

    dummy = ListNode()
    current = dummy

    for number in reversed(result):
        current.next = ListNode(int(number))
        current = current.next
            
    return dummy.next

addTwoNumbers(l1, l2)