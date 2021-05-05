
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_with_cache(n: int, memo: dict) -> int:
    if n in memo:
        return memo[n]

    memo[n] = fibonacci_with_cache(n - 1, memo) + \
        fibonacci_with_cache(n - 2, memo)

    return memo[n]

if __name__ == '__main__':
    #print(fibonacci(10))
    print(fibonacci_with_cache(10, {0: 0, 1: 1}))