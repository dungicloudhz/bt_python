def solve():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        s = input().strip()
        
        subsets = []
        limit = 1 << n
        for mask in range(1, limit):  # từ 1 → 2^n - 1 (bỏ tập rỗng)
            subset = []
            for i in range(n):
                if (mask >> i) & 1:
                    subset.append(s[i])
            subsets.append("".join(subset))
        
        # sort theo từ điển
        subsets.sort()
        print(" ".join(subsets))


solve()