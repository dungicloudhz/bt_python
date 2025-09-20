def lcs_length(S1, S2):
    n = len(S1)
    m = len(S2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if S1[i-1] == S2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

def solve():
    T = int(input())
    for _ in range(T):
        S1 = input().strip()
        S2 = input().strip()
        print(lcs_length(S1, S2))

if __name__ == "__main__":
    solve()
