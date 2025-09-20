def longest_increasing_decreasing(A, B):
    N = len(A)
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if A[j] < A[i] and B[j] > B[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = []
        B = []
        for _ in range(N):
            a = float(data[idx])
            b = float(data[idx+1])
            idx += 2
            A.append(a)
            B.append(b)
        results.append(longest_increasing_decreasing(A, B))
    
    for res in results:
        print(res)

if __name__ == "__main__":
    solve()
