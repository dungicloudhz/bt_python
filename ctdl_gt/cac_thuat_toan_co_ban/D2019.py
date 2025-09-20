def solve():
    T = int(input())
    def f(n, k):
        if n == 1:
            return 1
        mid = 2**(n-1) - 1
        if k == mid + 1:
            return n
        elif k <= mid:
            return f(n-1, k)
        else:
            return f(n-1, k - mid - 1)
    for _ in range(T):
        N, K = map(int, input().split())
        print(f(N, K))

if __name__ == "__main__":
    solve()
