def max_non_overlapping(segments):
    # Sắp xếp theo điểm kết thúc
    segments.sort(key=lambda x: x[1])
    
    count = 0
    last_end = -1
    
    for start, end in segments:
        if start >= last_end:
            count += 1
            last_end = end
    return count

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    
    T = int(data[idx])
    idx += 1
    
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        segments = []
        for _ in range(N):
            X1 = int(data[idx])
            X2 = int(data[idx+1])
            idx += 2
            segments.append((X1, X2))
        results.append(max_non_overlapping(segments))
    
    for res in results:
        print(res)

if __name__ == "__main__":
    solve()
