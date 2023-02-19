"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
from typing import List

class Solution:
    """
    O(n)
    """
    def searchInsert1(self, nums: List[int], target: int) -> int:
        size = len(nums)
        insertIndex = 0

        while insertIndex < size:
            if target <= nums[insertIndex]:
                return insertIndex
            else:
                insertIndex += 1

        return insertIndex

    """
    O(log(n))
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        nl, nr = 0, len(nums) - 1

        while nl <= nr:
            nm = (nl + nr) // 2
            if nums[nm] == target:
                return nm
            elif nums[nm] < target:
                nl = nm + 1
            else:
                nr = nm - 1
        return nl

def main():
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 5)) # 2
    print(sol.searchInsert([1,3,5,6], 2)) # 1
    print(sol.searchInsert([1,3,5,6], 7)) # 4
    print(sol.searchInsert([1,3,5,6], -3)) # 0

if __name__ == '__main__':
    main()