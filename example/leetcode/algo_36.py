from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        n = len(board)

        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    b = "(" + board[i][j] + ")"
                    addCount = 0
                    if (b + str(i)) not in seen:
                        seen.add(b + str(i))
                        addCount += 1
                    if (str(j) + b) not in seen:
                        seen.add(str(j) + b)
                        addCount += 1
                    if (str(i // 3) + b + str(j // 3)) not in seen:
                        seen.add(str(i // 3) + b + str(j // 3))
                        addCount += 1
                    if addCount != 3:
                        return False
        return True


if __name__ == '__main__':
    data = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    print(s.isValidSudoku(data))