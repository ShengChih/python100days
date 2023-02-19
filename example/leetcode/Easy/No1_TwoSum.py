"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List


class Solution:
    """
    Approach 1: Brute Force
    """
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

    """
    Approach 2: Two-pass Hash Table
    """
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

    """
    Approach 3: One-pass Hash Table
    """
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

    """
    若有相同 val，最優先 index 回傳
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in memo:
                if type(memo[diff]) == int or float:
                    return [memo[diff], i]
                else:
                    return [memo[diff][0], i]

            if nums[i] in memo:
                if type(memo[nums[i]]) == int or float:
                    memo[nums[i]] = [memo[nums[i]], i]
                else:
                    memo[nums[i]].append(i)
            else:
                memo[nums[i]] = i

        return []


def main():
    my = Solution()
    # case 1
    print(my.twoSum([2, 7, 11, 15], 9))

    # case 2
    print(my.twoSum([3,2,4], 6))

    # case 3
    print(my.twoSum([3, 3], 6))

if __name__ == '__main__':
    main()