# 醜數: 因數有 2, 3, 5

class Solution:
    def isUgly1(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 2 == 0:
            n /= 2

        while n % 3 == 0:
            n /= 3

        while n % 5 == 0:
            n /= 5

        return n == 1


    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        divers = [2, 3, 5]

        for i in range(len(divers)):
            diver = divers[i]

            while n % diver == 0:
                n //= diver

            i += 1

        return n == 1


def main():
    sol = Solution()
    print(sol.isUgly(17)) # False
    print(sol.isUgly(15)) # True
    print(sol.isUgly(9)) # True
    print(sol.isUgly(4)) # True
    print(sol.isUgly(20)) # True
    print(sol.isUgly(21)) # False
    print(sol.isUgly(14)) # False

if __name__ == '__main__':
    main()