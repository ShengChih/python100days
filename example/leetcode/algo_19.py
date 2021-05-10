# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        p = head

        def relink(node):
            if node == None:
                return 0

            nth = relink(node.next) + 1

            if nth > n:
                node.next.val = node.val

            return nth
        relink(p)
        return p.next

    def removeNthFromEnd2(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    data = [1,2,3,4,5]
    head = None

    for i in range(len(data) - 1, -1, -1):
        head = ListNode(data[i], head)

    s = Solution()
    p = s.removeNthFromEnd1(head, 2)

    while p:
        print(p.val)
        p = p.next