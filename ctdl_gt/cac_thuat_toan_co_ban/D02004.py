from itertools import combinations

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    N, K = map(int, input_data[:2])
    A = input_data[2:]
    
    results = set()
    for comb in combinations(range(N), K):
        s = "".join(A[i] for i in comb)
        results.add(s)
    
    for val in sorted(results):
        print(val)

if __name__ == "__main__":
    solve()
