"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pt = res = head
        curr = head.next if head else None

        while curr:
            if pt.val == curr.val:
                pt.next = None
            else:
                pt.next = curr
                pt = curr
            curr = curr.next

        return res


def toListNode(nums: List) -> Optional[ListNode]:
    size = len(nums)
    res = None

    for i in range(size - 1, -1, -1):
        node = ListNode(val=nums[i])
        node.next = res

        res = node

    dumpListNode(res)
    return res


def dumpListNode(head: ListNode):
    res = []
    while head:
        res.append(head.val)
        head = head.next

    print(res)

def main():
    sol = Solution()
    #dumpListNode(sol.deleteDuplicates(toListNode([1,1,2])))
    dumpListNode(sol.deleteDuplicates(toListNode([1,1,2,3,3])))


if __name__ == '__main__':
    main()