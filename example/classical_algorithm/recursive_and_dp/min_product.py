
def min_product(m: int, n: int) -> int:
    small, bigger = (m, n) if m < n else (n, m)
    
    return f_definition(small, bigger, {0:0, 1:n})

def f_definition(m: int, n: int, memo: dict) -> int:
    print("f(%d, %d)" % (m, n))
    if m in memo:
        return memo[m]

    s = m >> 1
    if s not in memo:
        memo[s] = f_definition(s, n, memo)

    halfProd = memo[s]

    return ((halfProd + halfProd) if m % 2 == 0 else (halfProd + halfProd + n))


if __name__ == '__main__':
    print(min_product(99, 102))