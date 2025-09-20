from itertools import combinations

def solve():
    T = int(input().strip())
    for _ in range(T):
        N, K = map(int, input().split())
        combs = list(combinations(range(1, N+1), K))
        for c in reversed(combs):
            print(" ".join(map(str, c)))
solve()