from typing import List
from collections import Counter

class Solution:
    # method 1
    def fourSumCount1(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        AB = Counter(a+b for a in nums1 for b in nums2)
        return sum(AB[-c-d] for c in nums3 for d in nums4)

    def fourSumCount2(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter = {}

        for i in nums1:
            for j in nums2:
                counter[i + j] = counter.get(i + j, 0) + 1

        res = 0
        for k in nums3:
            for l in nums4:
                res += counter.get(-k-l, 0)

        return res

if __name__ == '__main__':
    s = Solution()
    #print(s.fourSumCount1([1,2], [-2,-1], [-1,2], [0,2]))
    print(s.fourSumCount2([1,2], [-2,-1], [-1,2], [0,2]))