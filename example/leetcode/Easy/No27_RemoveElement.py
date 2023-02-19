from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        insertIndex = 0

        for i in range(size):
            if nums[i] != val:
                nums[insertIndex] = nums[i]
                insertIndex += 1
                
        return insertIndex


def main():
    my = Solution()
    print(my.removeElement([3,2,2,3], 3))
    print(my.removeElement([0,1,2,2,3,0,4,2], 3))

if __name__ == '__main__':
    main()