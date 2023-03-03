from functools import cache
from typing import List
import sys

class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        n = len(nums)
        sum, max = 0, -sys.maxsize

        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                if sum > max:
                    max = sum

        return max


    def maxSubArray2(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = 0

        for num in nums:
            if sum < 0:
                sum = 0

            sum += num
            maxSum = max(sum, maxSum)

        return maxSum


    def maxSubArray3(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1], nums[0] + nums[1])

        mid = n // 2
        l = self.maxSubArray(nums[0:mid])
        r = self.maxSubArray(nums[mid+1:])
        lmax = rmax = 0

        # cross sum
        sum = 0
        for i in range(mid - 1, -1, -1):
            sum += nums[i]
            if sum > lmax:
                lmax = sum

        sum = 0
        for i in range(mid + 1, n):
            sum += nums[i]
            if sum > rmax:
                rmax = sum

        return max(l, r, lmax + rmax + nums[mid])
    

    def maxSubArray4(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
        return max(nums)


    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def pick(i: int, mustPick: bool) -> int:
            if i >= n: return 0 if mustPick else -sys.maxsize
            if mustPick:
                return max(0, nums[i] + pick(i + 1, True))
            return max(pick(i + 1, False), nums[i] + pick(i + 1, True))

        return pick(0, False)


def main():
    sol = Solution()

    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
    print(sol.maxSubArray([1])) # 1
    print(sol.maxSubArray([5,4,-1,7,8])) # 23
    print(sol.maxSubArray([-2,-1,-3,4,-1,-2,-1,-5,-4])) # 4
    print(sol.maxSubArray([-1,0,-2])) # 0

if __name__ == "__main__":
    main()