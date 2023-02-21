"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def visit(self, node, res):
        if node:
            self.visit(node.left, res)
            res.append(node.val)
            self.visit(node.right, res)

        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        self.visit(root, res)

        return res


    def inorderTraversalIter(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        stack = []
        p = root

        while p or stack:
            while p:
                stack.append(p)
                p = p.left

            p = stack.pop()
            res.append(p.val)
            p = p.right

        return res




def toTree(nums, i, n):
    if i >= n or nums[i] is None:
        return None

    root = TreeNode(nums[i])
    root.left = toTree(nums, 2 * i + 1, n)
    root.right = toTree(nums, 2 * i + 2, n)

    return root



def main():
    sol = Solution()
    nums = [1, None, 2, None, None, 3]
    n = len(nums)
    treeRoot = toTree(nums, 0, n)

    # 遞迴 recursive 版本
    print(sol.inorderTraversal(treeRoot))

    #
    print(sol.inorderTraversalIter(treeRoot))

if __name__ == "__main__":
    main()