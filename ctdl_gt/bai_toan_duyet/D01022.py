def solve():
    N, K = map(int, input().split())
    words = input().split()
    
    results = set()
    
    for i in range(N - K + 1):
        s = "".join(words[i:i+K])
        results.add(s)
    
    for w in sorted(results):
        print(w)


if __name__ == "__main__":
    solve()
