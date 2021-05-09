
class Solution:
    def __init__(self):
        self.mapping = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def intToRoman(self, num: int) -> str:
        res = ""

        for divided in self.mapping:
            while num > 0 and num >= divided:
                quotient = num // divided
                res += quotient * self.mapping[divided]
                num = num - (quotient * divided)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(1994))
    print(s.intToRoman(3894))