"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/description/

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

from typing import List

class Solution:
    """
    # Time Limit Exceeded
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = len(nums)

        for i in range(total):
            sum = 0
            for j in range(i, total, 1):
                sum += nums[j]
                if sum == k:
                    count += 1
            
        return count
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = { 0: 1 }
        sum, count = 0, 0

        for num in nums:
            sum += num
            count += hashmap.get(sum - k, 0)
            hashmap[sum] = hashmap.get(sum, 0) + 1

        return count
    


def main():
    # 只從最前端找
    my = Solution()
    # case 1
    print(my.subarraySum([1,1,1], 2))

    # case 2
    print(my.subarraySum([1,2,3], 3))

    # special case 1
    print(my.subarraySum([1,-1,0], 0))


if __name__ == '__main__':
    main()