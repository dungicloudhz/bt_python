def solve():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        result = []
        limit = 1 << n  # 2^n
        for mask in range(limit):
            num = []
            for i in range(n-1, -1, -1):  # bit cao -> thấp
                if (mask >> i) & 1:
                    num.append('8')
                else:
                    num.append('6')
            result.append("".join(num))
        
        print(len(result))
        print(" ".join(result))

solve()