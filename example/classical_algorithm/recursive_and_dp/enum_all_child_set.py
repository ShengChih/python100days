
def f(n: int) -> list:
    ret = [[[]], [[], [1]], [[], [1], [2], [1, 2]]]

    if n in ret:
        return ret[n]

    for i in range(3, n + 1):
        ret.append((ret[i - 1] + [(child.copy() + [i]) for child in ret[i - 1]]))

    return ret[n]

if __name__ == '__main__':
    print(f(10))
