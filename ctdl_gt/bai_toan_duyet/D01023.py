def solve():
    N = int(input().strip())
    A = input().split()
    
    results = set()
    
    for i in range(N):
        s = ""
        for j in range(i, N):
            s += A[j]
            results.add(s)
    
    for val in sorted(results):
        print(val)


if __name__ == "__main__":
    solve()
