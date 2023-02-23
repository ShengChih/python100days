from typing import List
import math


class Solution:
    def getPrimeNumbers(self, l: int, r: int) -> List:
        ret = []

        if (l == 0 or l == 1) and r >= 2:
            if r == 2:
                ret.append(2)
                return ret
            elif r >= 3:
                ret.append(2)
                ret.append(3)
                l = 5
        elif l == 2:
            ret.append(2)

            if r == 2:
                return ret
        elif l == 3:
            ret.extend([2, 3])
            l = 5
        elif l % 2 == 0:
            l += 1

        for num in range(l, r + 1, 2):
            if self.isPrime(num):
                ret.append(num)

        return ret


    def isPrime(self, m: int) -> bool:
        if m >= 5:
            # 6n + 5 = 6(n + 1) - 1
            # 6n + 1
            mod = m % 6
            if mod != 1 and mod != 5:
                return False

            for i in range(5, math.floor(math.sqrt(m)) + 1, 2):
                if m % i == 0 or m % (i + 2) == 0:
                    return False
        elif m == 1:
            return False
        elif m == 2 or m == 3:
            return True
        else:
            return False            

        return True

    def countPrimes1(self, n: int) -> int:
        """
        too slow
        """
        if n >= 4:
            c = 2
            for i in range(5, n):
                if self.isPrime(i):
                    c += 1
            return c
        elif n == 3:
            return 1

        return 0


    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        sqrtn = math.floor(n ** 0.5) + 1
        prime = [1] * n
        prime[0] = prime[1] = 0
        ans = 0

        for num in range(2, sqrtn):
            if not prime[num]:
                continue
            ans += 1
            prime[num*num:n:num] = [0] * ((n - 1) // num - num + 1)

        return ans + sum(prime[sqrtn:])

def main():
    sol = Solution()
    print(sol.isPrime(561))
    print(sol.isPrime(17))
    print(sol.countPrimes(561))
    print(sol.getPrimeNumbers(0, 561))
    print(sol.countPrimes1(561))
    print(sol.countPrimes(561))


if __name__ == "__main__":
    main()