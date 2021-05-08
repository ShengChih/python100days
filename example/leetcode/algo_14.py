import os
from typing import List

class Solution:
    # method 1
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        return os.path.commonprefix(strs)

    # method 2
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        minOrder = min(strs)
        maxOrder = max(strs)

        for i, char in enumerate(minOrder):
            if char != maxOrder[i]:
                return minOrder[:i]
        
        return minOrder

    # method 3
    def longestCommonPrefix3(self, strs: List[str]) -> str:
        res = ""

        n = len(strs)
        first = strs[0]

        for i, c in enumerate(first):
            for j in range(1, n):
                if strs[j][i] != c:
                    return res
            res += c

        return res

    # method 4
    def longestCommonPrefix4(self, strs: List[str]) -> str:
        res = ""

        for pair in zip(*data):
            if len(list(set(pair))) > 1:
                break
            res += pair[0]

        return res

if __name__ == '__main__':
    data = ["flower","flow","flight"]
    s = Solution()
    #print(s.longestCommonPrefix1(data))
    #print(s.longestCommonPrefix2(data))
    #print(s.longestCommonPrefix3(data))
    print(s.longestCommonPrefix4(data))
            