import sys
import bisect

def solve():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        N, K = int(input_data[idx]), int(input_data[idx+1])
        idx += 2
        A = list(map(int, input_data[idx:idx+N]))
        idx += N
        
        pos = bisect.bisect_left(A, K)
        if pos < N and A[pos] == K:
            results.append(str(pos+1))   # in ra vị trí 1-based
        else:
            results.append("NO")
    print("\n".join(results))

if __name__ == "__main__":
    solve()
