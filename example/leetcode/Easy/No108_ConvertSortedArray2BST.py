"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""


from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        size = len(nums)
        mid = size // 2

        if not nums:
            return None

        m = TreeNode(nums[mid])
        lnums = nums[:mid]
        rnums = nums[(mid+1):]
        m.left = self.sortedArrayToBST(lnums) if lnums else None
        m.right = self.sortedArrayToBST(rnums) if rnums else None

        return m



def main():
    sol = Solution()
    #sol.sortedArrayToBST([-10,-3,0,5,9])
    #sol.sortedArrayToBST([1,3])
    sol.sortedArrayToBST([3, 5, 8])


if __name__ == '__main__':
    main()