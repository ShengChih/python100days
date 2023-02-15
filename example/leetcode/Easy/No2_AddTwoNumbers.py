from typing import Optional, List
from math import floor

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        curr = dummyHead
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            l1n = l1.val if l1 else 0
            l2n = l2.val if l2 else 0

            sum = l1n + l2n + carry
            carry = sum // 10
            newNode = ListNode((sum - (carry * 10)))
            curr.next = newNode
            curr = newNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummyHead.next


def input2ListNodes(input: List[int]) -> Optional[ListNode]:
    head = None
    prev = None
    curr = None

    for i in range(len(input)):
        curr = ListNode(input[i])
        if head is None:
            prev = head = ListNode(input[i])
        else:
            prev.next = curr
            prev = curr

    return head or []

def printListNodes(l1: Optional[ListNode]):
    nl = []
    while l1 and l1 != None:
        nl.append(l1.val)
        l1 = l1.next
    return nl

def main():
    my = Solution()

    # case 1
    print(printListNodes(my.addTwoNumbers(input2ListNodes([2,4,3]), input2ListNodes([5,6,4]))))

    # case 2
    print(printListNodes(my.addTwoNumbers(input2ListNodes([0]), input2ListNodes([0]))))

    # case 3
    print(printListNodes(my.addTwoNumbers(input2ListNodes([9,9,9,9,9,9,9]), input2ListNodes([9,9,9,9]))))

    # extra case 4
    print(printListNodes(my.addTwoNumbers(input2ListNodes([9,9,9,9,9,9,9]), input2ListNodes([1]))))

    # extra case 5
    print(printListNodes(my.addTwoNumbers(input2ListNodes([1]), input2ListNodes([9,9,9,9,9,9,9]))))

if __name__ == '__main__':
    main()