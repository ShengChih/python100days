from typing import List

class Solution:
    def __init__(self):
        self.mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    # method 1
    def letterCombinations1(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(self.mapping[digits[0]])
        prev = self.letterCombinations1(digits[:-1])
        additional = self.mapping[digits[-1]]
        return [s + c for s in prev for c in additional]

    # method 2
    def dfs(self, digits: str, path: str, res: list):
        if not digits and path:
            res.append(path)
            return

        for c in self.mapping[digits[0]]:
            self.dfs(digits[1:], path + c, res)


    def letterCombinations2(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(self.mapping[digits[0]])

        res = []
        self.dfs(digits, "", res)

        return res
    
    # method 3
    def letterCombinations3(self, digits: str) -> List[str]:
        length = len(digits)
        res = []
        
        if (length == 0):
            return res
        
        def backtrack(idx, candidate, digits, res):
            if (idx == len(digits)):
                res.append(candidate)
                return
                
            for next_char in self.mapping[digits[idx]]:
                candidate += next_char
                # print(next_char)
                backtrack(idx+1, candidate, digits, self.mapping, res)
                candidate = candidate[0:-1]
        
        backtrack(0, "", digits, res)
        
        return res


if __name__ == '__main__':
    s = Solution()
    #print(s.letterCombinations1("234"))
    #print(s.letterCombinations2("234"))
    print(s.letterCombinations3("234"))