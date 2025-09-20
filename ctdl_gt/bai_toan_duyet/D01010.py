from itertools import product

def solve():
    N = int(input().strip())
    chars = ['A', 'B', 'C']
    
    for length in range(3, N+1):  # độ dài tối thiểu là 3
        for p in product(chars, repeat=length):
            s = "".join(p)
            if set(s) == {'A', 'B', 'C'}:  # phải đủ A, B, C
                a, b, c = s.count('A'), s.count('B'), s.count('C')
                if a <= b <= c:
                    print(s)

solve()