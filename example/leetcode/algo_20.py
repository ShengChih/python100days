
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        
        d = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        if n == 0 or n == 1:
            return False

        for i in range(n):
            if s[i] not in d:
                stack.append(s[i])
                continue
            if not stack or stack.pop() != d[s[i]]:
                return False

        return not stack


if __name__ == '__main__':
    s = Solution()
    d1 = "()[]{}"
    d2 = "([)]"
    d3 = "{[]}"

    print(s.isValid(d1))
    print(s.isValid(d2))
    print(s.isValid(d3))