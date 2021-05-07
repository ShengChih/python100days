from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res

        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t < 0:
                    l += 1
                    continue
                elif t > 0:
                    r -= 1
                    continue

                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while r > l and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1

        return res


        


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
