from itertools import combinations_with_replacement

def solve():
    n, k = map(int, input().split())
    for comb in combinations_with_replacement(range(1, n + 1), k):
        print(" ".join(map(str, comb)))

if __name__ == "__main__":
    solve()
