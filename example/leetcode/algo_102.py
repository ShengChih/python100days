from typing import List

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: 'TreeNode') -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [root]

        while True:
            child_queue = []
            stack = []

            while queue:
                node = queue.pop(0)
                if node.left != None:
                    child_queue.append(node.left)
                if node.right != None:
                    child_queue.append(node.right)
                stack.append(node.val)

            res.append(stack)

            if child_queue:
                queue = child_queue

            if not queue:
                break
                
        return res


def build_node(data: list, parent_idx: int, max_len: int) -> 'TreeNode':
    if parent_idx >= max_len or data[parent_idx] == None:
        return None

    l = 2 * parent_idx + 1
    r = l + 1

    l_node = build_node(data, l, max_len)
    r_node = build_node(data, r, max_len)

    return TreeNode(data[parent_idx], l_node, r_node)


if __name__ == '__main__':
    s = Solution()

    data = [3, 9, 20, None, None, 15, 7]
    n = len(data)

    if n > 0:
        root = build_node(data, 0, n)
        print(s.levelOrder(root))