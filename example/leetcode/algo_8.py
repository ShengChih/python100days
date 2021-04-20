#!/usr/bin/python3

class Solution:

    def myAtoi(self, s: str) -> int:
        strlen = len(s)
        idx = 0
        stack = []
        isNegative = False
        answer = 0

        for idx in range(strlen):
            if s[idx] == '-':
                if stack:
                    break
                stack.append(s[idx])
                isNegative = True
            elif s[idx] == '+':
                if stack:
                    break
                stack.append(s[idx])
            elif s[idx].isnumeric():
                stack.append(s[idx])
            elif s[idx] == '.':
                break
            elif s[idx] == ' ':
                if stack:
                    break
            else:
                break

        if stack and (stack[0] == '-' or stack[0] == '+'):
            stack = stack[1:]

        ret = ''.join(stack)
        ret = int(ret) if ret.isnumeric() else 0

        if isNegative:
            ret = -ret

        bound = 2 ** 31
        upperBound = bound - 1
        lowerBound = -bound

        if ret < lowerBound:
            return lowerBound
        elif ret > upperBound:
            return upperBound

        return ret
    
def main():
    solution = Solution()

    print(solution.myAtoi("42"))
    print(solution.myAtoi("42a"))
    print(solution.myAtoi("-14a"))
    print(solution.myAtoi("a14"))
    print(solution.myAtoi("a-14"))
    print(solution.myAtoi("-a14"))
    print(solution.myAtoi("    -14   "))
    print(solution.myAtoi("-     32"))
    print(solution.myAtoi("-1a21"))
    print(solution.myAtoi("+123a"))
    print(solution.myAtoi("+-12"))
    print(solution.myAtoi("-91283472332"))
    print(solution.myAtoi("91283472332"))
    print(solution.myAtoi("-+123"))
    print(solution.myAtoi("2-3"))
    print(solution.myAtoi("0.5"))
    print(solution.myAtoi("-4.3"))
    print(solution.myAtoi("-.3"))
    print(solution.myAtoi("  +  413"))

if __name__ == '__main__':
    main()