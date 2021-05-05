
def fibonacci(n: int) -> int:
    dp = [0, 1]

    for idx in range(2, n + 1):
        dp.append(dp[idx - 1] + dp[idx - 2])

    return dp[n]

if __name__ == '__main__':
    print(fibonacci(10))