#!/usr/bin/python3

from typing import List

class Solution:
    def findCombination(self, target: int, picks: List[int]):
        if target < 0:
            return

        for item in self.candidates:
            if target < item:
                return

            if picks and picks[-1] > item:
                continue

            if target == item:
                picks += [item]
                self.output.append(picks)
                return

            if target > item:
                self.findCombination(target - item, picks + [item])

        return

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sortedCandidates =  sorted(candidates)
        self.candidates = sortedCandidates
        self.output = []
        self.check = {}

        result = []
        picks = []

        self.findCombination(target, picks)

        return self.output

def main():
    solution = Solution()
    #print(solution.combinationSum([1], 1))
    #print(solution.combinationSum([2,3,6,7], 7))
    #print(solution.combinationSum([2,3,5], 8))


if __name__ == '__main__':
    main()