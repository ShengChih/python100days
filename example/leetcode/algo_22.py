from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def parenthesis(l: int, r: int, path: str):
            if not r and path:
                res.append(path)
                return

            if l:
                parenthesis(l - 1, r, path + "(")

            if r > l:
                parenthesis(l, r - 1, path + ")")

        parenthesis(n, n, "")
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))