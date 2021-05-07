from typing import List

class Solution:
    def find_combination(
        self,
        candidates: List[int],
        start: int,
        target: int,
        picks: List[int],
        res: List[List[int]]
    ):
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue

            if target < candidates[i]:
                return
            
            if target == candidates[i]:
                res.append(picks + [candidates[i]])
                return
            
            self.find_combination(
                candidates,
                i + 1,
                target - candidates[i],
                picks + [candidates[i]],
                res
            )

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        candidates.sort()
        res = []
        memo = {}

        self.find_combination(
            candidates,
            0,
            target,
            [],
            res
        )

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))