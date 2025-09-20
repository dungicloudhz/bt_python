import sys
from itertools import permutations

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    M = int(data[1])

    remaining = [i for i in range(1, N+1) if i != M]
    # remaining đã là thứ tự tăng -> permutations sẽ ra theo thứ tự từ điển
    for perm in permutations(remaining):
        out = list(perm) + [M]
        print(" ".join(map(str, out)))

if __name__ == "__main__":
    main()
