from typing import List

class Solution:
    # method 1
    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        # i + j = target - k - l
        for i in range(0, n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] * 4 > target or nums[n - 1] * 4 < target:
                break

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                if nums[j] * 3 > (target - nums[i]) or \
                    nums[n - 1] * 3 < (target - nums[i]):
                    break

                k = j + 1
                l = n - 1

                while k < l:
                    if nums[k] * 2 > (target - nums[i] - nums[j]) or \
                        nums[l] * 2 < (target - nums[i] - nums[j]):
                        break
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

    # method 2
    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        max_n = len(nums)

        def nSum(
            nums: List[int],
            target: int,
            l: int,
            r: int,
            n: int,
            picks: List[int],
            results: List[List[int]]
        ):
            if n < 2 or (r - l + 1) < n \
                or nums[l] * n > target or nums[r] * n < target:
                return

            if n == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s > target:
                        r -= 1
                        continue
                    elif s < target:
                        l += 1
                        continue

                    if s == target:
                        results.append(picks + [nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1
                return


            for i in range(l, r + 1):
                if i > l and nums[i] == nums[i - 1]:
                    continue
                nSum(nums, target - nums[i], i + 1, r, n - 1, picks + [nums[i]], results)

        nSum(nums, target, 0, max_n - 1, 4, [], res)

        return res


if __name__ == '__main__':
    s = Solution()
    #print(s.fourSum1([1,0,-1,0,-2,2], 0))
    print(s.fourSum2([1,0,-1,0,-2,2], 0))