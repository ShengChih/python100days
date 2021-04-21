#!/usr/bin/python3

class Solution:
    def reverse(self, x: int) -> int: 
        is_negative = True if x < 0 else False
        y = str(abs(x))
        y = int(y[::-1])
        
        bound = 2 ** 31
        
        if y >= bound:
            return 0
        elif y < -bound:
            return 0

        return -y if is_negative else y
 
def main():
    solution = Solution()
    print(solution.reverse(123))

if __name__ == '__main__':
    main()
