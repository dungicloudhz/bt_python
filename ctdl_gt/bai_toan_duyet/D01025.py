from itertools import combinations

def solve():
    T = int(input().strip())
    for _ in range(T):
        parts = input().strip().split()
        while len(parts) < 2:   # bỏ qua dòng trống nếu có
            parts = input().strip().split()
        S, K = parts[0], int(parts[1])
        N = len(S)
        results = set()
        for comb in combinations(range(N), K):
            num = "".join(S[i] for i in comb)
            results.add(num)
        for val in sorted(results, key=lambda x: int(x)):
            print(val)

if __name__ == "__main__":
    solve()
