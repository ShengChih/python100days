"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List

class Solution:
    def broutForceMaxProfit(self, prices: List[int]) -> int:
        length = len(prices)

        max_profit = 0

        for i in range(0, length):
            profit = 0
            for j in range(i+1, length):
                profit += (prices[j] - prices[j-1])
                print("%d - %d = %d" % (i, j, profit))
                if profit > max_profit:
                    max_profit = profit

        return max_profit

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


if __name__ == '__main__':
    s = Solution()
    #print(s.broutForceMaxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,1,5,3,6,4]))