def longest_repeated_subsequence(S):
    n = len(S)
    dp = [[0]*(n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if S[i-1] == S[j-1] and i != j:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][n]

def solve():
    T = int(input())
    for _ in range(T):
        _ = int(input())  # độ dài xâu, không cần dùng
        S = input().strip()
        print(longest_repeated_subsequence(S))

if __name__ == "__main__":
    solve()
