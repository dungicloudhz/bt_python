from itertools import combinations

def solve():
    N, K = map(int, input().split())
    A = input().split()
    
    results = set()
    
    for comb in combinations(range(N), K):
        s = "".join(A[i] for i in comb)
        results.add(s)
    
    for val in sorted(results):
        print(val)


if __name__ == "__main__":
    solve()
