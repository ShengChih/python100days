class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            n = -n
            x = 1 / x

        return x * self.myPow(x, n - 1) if n & 1 else self.myPow(x * x, n // 2)

if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2, 10))
    print(s.myPow(2, 11))