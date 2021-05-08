class Solution:
    def __init__(self):
        self.mapping = {
            "I": 1,
            "IV": 4,
            "IX": 9,
            "V": 5,
            "X": 10,
            "XL": 40,
            "XC": 90,
            "L": 50,
            "C": 100,
            "CD": 400,
            "CM": 900,
            "D": 500,
            "M": 1000,
        }

    # method 1
    def romanToInt1(self, s: str) -> int:
        res = 0
        n = len(s)
        
        for i in range(n):
            res += self.mapping[s[i]]
            if i > 0 and self.mapping[s[i - 1]] < self.mapping[s[i]]:
                res -= 2 * self.mapping[s[i-1]]
                
        return res
    
    # metho 2
    def romanToInt2(self, s: str) -> int:
        res = 0
        n = len(s)
        i = 0

        while i < n:
            if i < n - 1 and (s[i] + s[i + 1] in self.mapping):
                res += self.mapping[s[i] + s[i + 1]]
                i += 2
            else:
                res += self.mapping[s[i]]
                i += 1
                
        return res

    # method 3
    def romanToInt3(self, s: str) -> int:
        res, prev = 0, 0
        for i in s[::-1]:
            if self.mapping[i] >= prev:
                res += self.mapping[i]
            else:
                res -= self.mapping[i]
            prev = self.mapping[i]
        return res

    # method 4
    def romanToInt(self, s: str) -> int:
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += self.mapping[char]
        return number


if __name__ == '__main__':
    s = Solution()
    #print(s.romanToInt2("IV"))
    #print(s.romanToInt2("LIV"))
    #print(s.romanToInt2("CL"))
    #print(s.romanToInt2("MCMXCIV"))
    #print(s.romanToInt2("MDCXCV"))