"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            arr = [0] * (i+1)
            arr[0] = arr[-1] = 1
            preArr = res[-1]

            for j in range(1, (i // 2) + 1):
                arr[j] = arr[i - j] = preArr[j - 1] + preArr[j]
            res.append(arr)

        return res


def main():
    sol = Solution()
    print(sol.generate(5))
    print(sol.generate(1))


if __name__ == "__main__":
    main()