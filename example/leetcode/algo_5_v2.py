#!/usr/bin/python3

class Solution:
    # method 1
    def palindrome_str(self, s: str, strlen: int, l: int, r: int) -> str:
        while l >= 0 and r < strlen and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]
    
    def longestPalindrome1(self, s: str) -> str:
        strlen = len(s)

        res = ""

        for i in range(strlen):
            odd = self.palindrome_str(s, strlen, i, i)
            even = self.palindrome_str(s, strlen, i, i + 1)

            res = max(res, odd, even, key=len)

        return res
    
    #method 2
    def longestPalindrome2(self, s: str) -> str:
        strlen = len(s)

        if strlen == 0 or strlen == 1:
            return s
        elif strlen == 2:
            return s if s[0] == s[1] else s[0]

        dp = [[False] * strlen for i in range(strlen)]
        for i in range(strlen):
            dp[i][i] = True

        maxLen = i = j = 0
        ans = ""
        
        for i in range(strlen - 2, -1, -1):
            for j in range(i + 1, strlen):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True

                        if len(ans) < j - i + 1:
                            ans = s[i:j+1]

        return ans


def main():
    solution = Solution()
    #print(solution.longestPalindrome1('cbbd'))
    #print(solution.longestPalindrome1('abc'))
    #print(solution.longestPalindrome1('ac'))
    #print(solution.longestPalindrome1('acbcbcbcabacasadwq'))
    #print(solution.longestPalindrome1('aa'))
    #print(solution.longestPalindrome2('a'))
    #print(solution.longestPalindrome2('bba123321abc'))
    #print(solution.longestPalindrome2("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
    #print(solution.longestPalindrome2("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))

if __name__ == '__main__':
    main()