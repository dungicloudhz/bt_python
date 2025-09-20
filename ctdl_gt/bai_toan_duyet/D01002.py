def solve():
    n = int(input().strip())
    limit = 1 << n   # 2^n
    
    for x in range(limit):
        s = []
        for i in range(n-1, -1, -1):  # từ bit cao xuống thấp
            if (x >> i) & 1:
                s.append("B")
            else:
                s.append("A")
        if "A" in s and "B" in s:
            print("".join(s))

solve()