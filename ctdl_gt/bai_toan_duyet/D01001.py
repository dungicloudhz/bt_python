def solve():
    n = int(input().strip())
    limit = 1 << n   # 2^n
    
    for x in range(limit):
        binary = format(x, f'0{n}b')  # dạng chuỗi nhị phân, đủ n bit
        if binary.count("1") % 2 == 0:
            print(" ".join(binary))

solve()