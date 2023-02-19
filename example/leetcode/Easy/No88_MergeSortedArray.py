"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        size1 = min(len(nums1), m)
        size2 = min(len(nums2), n)

        i, j, n = size1 - 1, size2 - 1, (size1 + size2 - 1)

        while n >= 0:
            n1 = nums1[i] if i >= 0 else None
            n2 = nums2[j] if j >= 0 else None

            if n1 is not None and n2 is not None:
                if n1 < n2:
                    tmp = n2
                    j -= 1
                else:
                    tmp = n1
                    i -= 1
            elif n2 is not None:
                tmp = n2
                j -= 1
            else:
                tmp = n1
                i -= 1

            nums1[n] = tmp
            n -= 1

        print(nums1)

                    


def main():
    sol = Solution()
    sol.merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)
    sol.merge(nums1=[1], m=1, nums2=[0], n=0)
    sol.merge(nums1=[0], m=0, nums2=[1], n=1)
    sol.merge(nums1=[4,5,6,0,0,0], m=3, nums2=[1,2,3], n=3)

if __name__ == "__main__":
    main()
