
def f(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return f(n - 1) + f(n - 2) + f(n - 3)

def f_with_cache(n: int, memo: dict) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n in memo:
        return memo[n]

    memo[n] = f(n - 1) + f(n - 2) + f(n - 3)
    return memo[n]

def f_dp(n: int) -> int:
    dp = [0, 1, 2, 4]

    for i in range(4, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

    return dp[n]

if __name__ == '__main__':
    #print(f(10))
    #print(f_with_cache(10, {-1:0, 0:0, 1:1, 2:2, 3:4}))
    print(f_dp(10))