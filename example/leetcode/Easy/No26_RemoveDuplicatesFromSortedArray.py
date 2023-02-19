from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        insertIndex = 1

        for i in range(1, size):
            if nums[i - 1] != nums[i]:
                nums[insertIndex] = nums[i]
                insertIndex += 1

        return insertIndex

def main():
    my = Solution()
    print(my.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

if __name__ == '__main__':
    main()