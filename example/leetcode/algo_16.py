from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        res = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            j, k = i + 1, n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == target:
                    return s

                if abs(s - target) < abs(res - target):
                    res = s

                if s < target:
                    j += 1
                else:
                    k -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    s.threeSumClosest([-1,2,1,-4], 1)