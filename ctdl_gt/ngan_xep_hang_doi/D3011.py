import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    nums = list(map(int, data[1:]))
    out = []
    for n in nums:
        binaries = [bin(i)[2:] for i in range(1, n+1)]
        out.append(" ".join(binaries))
    print("\n".join(out))

if __name__ == "__main__":
    solve()
