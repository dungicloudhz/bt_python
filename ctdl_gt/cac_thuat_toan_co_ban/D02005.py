import sys

def solve():
    data = [x for x in sys.stdin.read().strip().split() if x]
    if not data:
        return
    t = int(data[0])
    vals = list(map(int, data[1:1+t]))
    denoms = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    out = []
    for N in vals:
        cnt = 0
        remaining = N
        for d in denoms:
            if remaining == 0:
                break
            use = remaining // d
            if use:
                cnt += use
                remaining -= use * d
        out.append(str(cnt))
    print("\n".join(out))

if __name__ == "__main__":
    solve()
