MOD = 10**9 + 7

def mod_pow(n, k, mod):
    res = 1
    n %= mod
    while k > 0:
        if k & 1:
            res = (res * n) % mod
        n = (n * n) % mod
        k >>= 1
    return res

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    T = int(input_data[0])
    idx = 1
    results = []
    for _ in range(T):
        N, K = int(input_data[idx]), int(input_data[idx+1])
        idx += 2
        results.append(str(mod_pow(N, K, MOD)))
    print("\n".join(results))

if __name__ == "__main__":
    solve()
