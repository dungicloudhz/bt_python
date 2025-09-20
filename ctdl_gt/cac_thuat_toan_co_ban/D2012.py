def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    M = int(data[1])
    
    items = []
    idx = 2
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx+1])
        items.append((x, y))
        idx += 2
    
    dp = [0] * (M + 1)
    
    for weight, value in items:
        for w in range(M, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    
    print(dp[M])

if __name__ == "__main__":
    solve()
