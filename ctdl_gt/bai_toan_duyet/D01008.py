from itertools import combinations

def solve():
    n, k = map(int, input().split())
    for comb in combinations(range(1, n+1), k):
        if sum(comb) % 2 == 0:  # tổng chẵn
            print(" ".join(map(str, comb)))

solve()