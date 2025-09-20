import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    res = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        jobs = []
        for _ in range(n):
            a = int(data[idx]); b = int(data[idx+1])
            jobs.append((a, b))
            idx += 2
        # Sắp xếp theo thời gian kết thúc
        jobs.sort(key=lambda x: x[1])
        count = 0
        last_end = -1
        for a, b in jobs:
            if a >= last_end:
                count += 1
                last_end = b
        res.append(str(count))
    print("\n".join(res))

if __name__ == "__main__":
    solve()
