
# method 1
def permutation(s: str):
    strlen = len(s)

    if strlen == 1:
        return [s]
    elif strlen == 2:
        return [s[0] + s[1], s[1] + s[0]]

    ret = {}

    for i in range(0, strlen):
        c = s[i]
        for parial in permutation(s[:i] + s[i+1:]):
            origin = list(parial)
            for insertIdx in range(0, len(parial) + 1):
                target = origin.copy()
                target.insert(insertIdx, c)
                newWord = ''.join(target)
                if newWord not in ret:
                    ret[newWord] = 1

    return [*ret.keys()]

# method 2
def in_permutation(prefix: str, remainder: str, ret: dict):
    strlen = len(remainder)

    if strlen == 0:
        if prefix and prefix not in ret:
            ret[prefix] = 1
        return
    
    for i in range(0, strlen):
        before = remainder[:i]
        after = remainder[i+1:]
        c = remainder[i]
        in_permutation(prefix + c, before + after, ret)

if __name__ == '__main__':
    #print(permutation('abcd'))
    results = {}
    in_permutation("", 'abcd', results)
    print([*results.keys()])