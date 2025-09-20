import math
from itertools import combinations
import sys

def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    r = int(math.isqrt(x))
    for i in range(3, r+1, 2):
        if x % i == 0:
            return False
    return True

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N, K = map(int, data[:2])
    idx = 1
    for comb in combinations(range(1, N+1), K):
        if is_prime(idx):
            print(f"{idx}: {' '.join(map(str, comb))}")
        idx += 1

if __name__ == "__main__":
    main()
