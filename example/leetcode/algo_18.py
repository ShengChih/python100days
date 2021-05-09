from typing import List

class Solution:
    # method 1
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        # i + j = target - k - l
        for i in range(0, n - 3):
            if nums[i] * 4 > target or nums[n - 1] * 4 < target:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = j + 1
                l = n - 1

                while k < l:
                    s = nums[i] + nums[j]
                    t = target - nums[k] - nums[l]

                    if s > t:
                        l -= 1
                        continue
                    elif s < t:
                        k += 1
                        continue

                    res.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1

                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                
                    while l > k and nums[l] == nums[l + 1]:
                        l -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1,0,-1,0,-2,2], 0))