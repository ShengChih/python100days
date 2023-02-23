from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        p = head

        while list1 or list2:
            n1 = list1
            n2 = list2

            if n1 and n2:
                if n1.val <= n2.val:
                    list1, p.next = n1.next, n1
                else:
                    list2, p.next = n2.next, n2
                p = p.next
            elif n1:
                p.next = n1
                break
            elif n2:
                p.next = n2
                break
            
        return head.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val <= list2.val:
                list1.next = self.mergeTwoLists2(list1.next, list2)
                return list1
            list2.next = self.mergeTwoLists2(list1, list2.next)
            return list2
        elif list1:
            return list1
        elif list2:
            return list2

        return None



def toLinkList(nums: List):
    head = ListNode()
    p = head

    for i in nums:
        p.next = node = ListNode(i)
        p = node

    return head.next


def main():
    l1 = [1,2,4]
    l2 = [1,3,4,5,6]
    sol = Solution()
    sol.mergeTwoLists(toLinkList(l1), toLinkList(l2))


if __name__ == "__main__":
    main()