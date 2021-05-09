from collections import Counter

class Solution:
    # method 1
    def fourSumCount(self, A, B, C, D):
        AB = Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)

if __name__ == '__main__':
    s = Solution()
    print(s.fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))