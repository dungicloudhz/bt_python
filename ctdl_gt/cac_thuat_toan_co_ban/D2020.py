import heapq

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        ropes = list(map(int, data[idx:idx+N]))
        idx += N
        
        heapq.heapify(ropes)
        cost = 0
        
        while len(ropes) > 1:
            a = heapq.heappop(ropes)
            b = heapq.heappop(ropes)
            cost += a + b
            heapq.heappush(ropes, a + b)
        
        results.append(str(cost))
    
    print('\n'.join(results))

if __name__ == "__main__":
    solve()
