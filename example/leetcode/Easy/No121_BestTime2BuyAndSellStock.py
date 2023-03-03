from typing import List
import sys

class Solution: 
    def maxProfit1(self, prices):
        """
        暴力解太慢
        """
        n, max = len(prices), 0

        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]

                if profit > max:
                    max = profit


        return max


    def maxProfit2(self, prices):
        """
        單純 DP，但太慢
        """
        n, max = len(prices), 0
        
        dp = [[0] * n  for _ in range(n)] 
        i, j = 0, 1
        # l, r = 0, 0

        for (e1, e2) in zip(prices[1:], prices[0: n-1]):
            diff = e1 - e2
            dp[i][j] = diff
            if diff > max:
                max = diff
                # l, r = i, j
            i, j = i + 1, j + 1

        for i in range(n):
            for j in range(i + 2, n):
                dp[i][j] = dp[i][j - 1] + dp[j - 1][j]
                
                if dp[i][j] > max:
                    max = dp[i][j]
                    # l, r = i, j

        # print(l, r)
        return max

    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        max_profit = 0

        if (length == 0):
            return max_profit

        min_value = prices[0]

        for i in range(1, length):
            if prices[i] < min_value:
                min_value = prices[i]

            if min_value < prices[i] and (prices[i] - min_value) > max_profit:
                max_profit = prices[i] - min_value

        return max_profit

def maxSubSum1(nums):
    n = len(nums)
    sum, max = 0, -sys.maxsize

    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum > max:
                max = sum

    return max

def maxSubSum(nums):
    n = len(nums)
    mid = (n - 1) // 2
    s = 1

    lsum = lmax = nums[mid - s] if mid - 1 >= 0 else None
    rsum = rmax = nums[mid + s] if mid + 1 < n else None

    for s in range(2, n - mid):
        if lmax is not None and mid - s >= 0:
            lmax = max(nums[mid-s], lsum, nums[mid-s] + lsum)

        if rmax is not None and mid + s < n:
            rmax = max(nums[mid+s], rsum, rsum + nums[mid+s])

    mmax = nums[mid]


    if lmax is not None and rmax is not None:
        return max(lmax + mmax, rmax + mmax, lmax + rmax + mmax, mmax, lmax, rmax)
    elif lmax is not None:
        return max(lmax, lmax + mmax, mmax)
    elif rmax is not None:
        return max(rmax, rmax + mmax, mmax)

    return nums[mid]

if __name__ == "__main__":
    sol = Solution()
    # print(sol.maxProfit2([7,1,5,3,6,4])) # 5
    # print(sol.maxProfit2([7,6,4,3,1])) # 0

    print(maxSubSum([-2,1,-3,4,-1,2,1,-5,4])) # 6
    print(maxSubSum([10,-5,7,6,-1,-3])) # 18
    print(maxSubSum([5,4,-1,7,8])) # 23
    print(maxSubSum([-1,-2])) # -1
    print(maxSubSum([-2,-1,-3,-4,1,-2,-1,-5,-4])) # 1
    print(maxSubSum([8,-19,5,-4,20])) # 21
    print(maxSubSum([-2,-1,-3,4,-1,-2,-1,-5,-4])) # 4
    print(maxSubSum([-1,-2,-3,0])) # 0
