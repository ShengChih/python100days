#!/usr/bin/python3

class Solution:

    def _findStr(self, i, j) -> int:
        if i == j:
            return 1
        elif i > j:
            return 0
        elif -1 != self.dp[i][j]:
            return self.dp[i][j]

        """
        if 兩邊的字元一樣, 左右範圍在縮小
        elif 左邊縮小的 case 好
        elif 右邊縮小的 case 好
        else 左邊右邊縮小後, 長度相同, 任選一邊即可

        f(x, y) = ?

        case 1:
            x == y, return 1
        case 2:
            x > y, return 0
        case 3:
            s[x] == s[y]
            # 簡易檢查目前字串回文，兩邊縮內的長度是不是恰好大於等於(字串總長 - 1)
            f(x, y) = (
                f(x + 1, y - 1) >= (j - i - 1)
                ? f(x + 1, y - 1) + (x == y ? 1 : 2)
                : max(f(i + 1, j), f(i, j -1))
            )
        """

        # pTb: left: 1, right 2, both:0, init: -1
        strlen = -1

        if self._findStr(i + 1, j) >= self._findStr(i, j - 1):
            strlen = self._findStr(i + 1, j)
            self.pTb[i][j] = 1
        else:
            strlen = self._findStr(i, j - 1)
            self.pTb[i][j] = 2

        if self.input[i] == self.input[j]:
            midSide = self._findStr(i + 1, j - 1)
            midLen = (j - 1) - (i + 1) + 1

            if midSide >= midLen:
                strlen = midSide + (1 if i == j else 2)
                self.pTb[i][j] = 0

        self.dp[i][j] = strlen

        return self.dp[i][j]


    def _printStr(self, i, j):
        s = ''
        if (j - i) <= 1:
            return self.input[i:(j + 1)]

        if i == j:
            return self.input[i]
        elif 0 == self.pTb[i][j]:
            return self.input[i: (i+1)] + \
                self._printStr(i + 1, j - 1) + \
                self.input[j: (j+1)]
        elif 1 == self.pTb[i][j]:
            return self._printStr(i + 1, j)

        return self._printStr(i, j - 1)


    def longestPalindrome(self, s: str) -> str:
        self.input = s
        strlen = len(s)

        self.dp = [ [-1] * strlen for idx in range(strlen) ]
        self.pTb = [ [-1] * strlen for idx in range(strlen) ]

        maxLen = self._findStr(0, strlen - 1)
        maxStr = self._printStr(0, strlen - 1)

        print('max length: %d' % maxLen)

        return maxStr

def main():
    solution = Solution()
    print(solution.longestPalindrome('acbcbcbcabacasadwq'))
    print(solution.longestPalindrome('aa'))
    print(solution.longestPalindrome('a'))
    print(solution.longestPalindrome('bba123321abc'))


if __name__ == '__main__':
    main()