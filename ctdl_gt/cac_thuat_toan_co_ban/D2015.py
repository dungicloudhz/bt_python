def max_loot(A):
    n = len(A)
    if n == 0:
        return 0
    elif n == 1:
        return A[0]
    
    prev2 = A[0]
    prev1 = max(A[0], A[1])
    
    for i in range(2, n):
        curr = max(prev1, prev2 + A[i])
        prev2, prev1 = prev1, curr
    return prev1

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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        results.append(max_loot(A))
    
    for res in results:
        print(res)

if __name__ == "__main__":
    solve()
