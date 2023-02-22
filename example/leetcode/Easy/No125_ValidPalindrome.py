class Solution:
    def isLetterOrDigit(self, c: str):
        ascii = ord(c)

        if ascii in range(97, 123) or ascii in range(65, 91) or ascii in range(48, 58):
            return True

        return False


    def isPalindrome1(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        lc = rc = None

        while l < r:
            lc = s[l]
            rc = s[r]


            if not self.isLetterOrDigit(s[l]):
                l += 1
            elif not self.isLetterOrDigit(s[r]):
                r -= 1
            else:
                if lc != rc:
                    return False
                l += 1
                r -= 1

        return True

    def isPalindrome2(self, s: str) -> bool:
        import re
        data = re.sub(r'[^0-9a-zA-Z]', '', s)
        return data.lower() == data[::-1].lower()


    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        ns = ''

        for i in range(n):
            c = s[i]
            if c >= 'a' and c <= 'z':
                ns += c
            elif c >= 'A' and c <= 'Z':
                ns += c.lower()
            elif c >= '0' and c <= '9':
                ns += c

        j = len(ns)
        for i in range(j):
            if ns[i] != ns[j - i - 1]:
                return False

        return True

def main():
    sol = Solution()
    print(sol.isPalindrome("9,8"))
    print(sol.isPalindrome("0P"))
    print(sol.isPalindrome("."))
    print(sol.isPalindrome(".,"))
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print(sol.isPalindrome("race a car"))
    print(sol.isPalindrome(" "))


if __name__ == "__main__":
    main()