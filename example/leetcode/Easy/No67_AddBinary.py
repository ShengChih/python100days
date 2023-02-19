"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [*a]
        b = [*b]
        i = len(a)
        j = len(b)
        n = max(i, j)
        res = [0] * n
        n -= 1
        i -= 1
        j -= 1
        carry = 0

        while n >= 0:
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1

            if j >= 0:
                sum += int(b[j])
                j -= 1

            carry = sum // 2
            res[n] = str(sum - carry * 2)
            n -= 1

        return (str(carry) if carry > 0 else '') + ''.join(res)

"""
 他解:先加總後反轉字串
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1
      s.append(str(carry % 2))
      carry //= 2

    return ''.join(reversed(s))
"""


def main():
    sol = Solution()
    print(sol.addBinary("11", "1"))
    print(sol.addBinary("1010", "1011"))
    print(sol.addBinary("0", "0"))


if __name__ == '__main__':
    main()