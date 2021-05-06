
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)

        if length == 0 or length == 1:
            return 0

        max_profit = 0
        for i in range(1, length):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))