from itertools import product

def solve():
    n = int(input().strip())
    alphabet = ['0', '1', '2']
    idx = 1
    for p in product(alphabet, repeat=n):
        if idx % 2 == 0:
            print(f"{idx}: {''.join(p)}")
        idx += 1

solve()