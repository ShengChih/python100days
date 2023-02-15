from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in memo:
                if type(memo[diff]) == int or float:
                    return [memo[diff], i]
                else:
                    return [memo[diff][0], i]

            if nums[i] in memo:
                if type(memo[nums[i]]) == int or float:
                    memo[nums[i]] = [memo[nums[i]], i]
                else:
                    memo[nums[i]].append(i)
            else:
                memo[nums[i]] = i

        return []

class BestAnswer:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i

def main():
    my = Solution()
    # case 1
    print(my.twoSum([2, 7, 11, 15], 9))

    # case 2
    print(my.twoSum([3,2,4], 6))

    # case 3
    print(my.twoSum([3, 3], 6))

    best = BestAnswer()
    # case 1
    print(best.twoSum([2, 7, 11, 15], 9))

    # case 2
    print(best.twoSum([3,2,4], 6))

    # case 3
    print(best.twoSum([3, 3], 6))

if __name__ == '__main__':
    main()