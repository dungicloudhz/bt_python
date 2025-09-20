from itertools import combinations

def solve():
    N, K = map(int, input().split())
    nums = range(1, N+1)
    for idx, comb in enumerate(combinations(nums, K)):
        if idx % K == 0:
            print(" ".join(map(str, comb)))

if __name__ == "__main__":
    solve()
