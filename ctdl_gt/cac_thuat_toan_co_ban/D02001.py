def solve():
    import sys
    data = [line.strip() for line in sys.stdin if line.strip()]  # bỏ dòng trống
    
    t = int(data[0])
    results = []
    idx = 1
    for _ in range(t):
        n = int(data[idx]); idx += 1
        arr = list(map(int, data[idx].split())); idx += 1
        arr.sort()
        results.append(" ".join(map(str, arr)))
    print("\n".join(results))


if __name__ == "__main__":
    solve()
