MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    tests = []
    max_n = 0
    idx = 1
    for _ in range(t):
        N = int(data[idx])
        K = int(data[idx+1])
        tests.append((N, K))
        max_n = max(max_n, N)
        idx += 2
    
    # Xử lý từng test
    for N, K in tests:
        dp = [0] * (N + 1)
        dp[0] = 1
        window_sum = 1  # dp[0]
        for i in range(1, N + 1):
            dp[i] = window_sum % MOD
            window_sum = (window_sum + dp[i]) % MOD
            if i >= K:
                window_sum = (window_sum - dp[i - K] + MOD) % MOD
        print(dp[N])

if __name__ == "__main__":
    solve()
