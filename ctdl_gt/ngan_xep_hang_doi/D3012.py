from collections import deque

def smallest_multiple(N):
    # BFS theo dư mod N
    visited = [False] * (N + 1)
    parent = [-1] * (N + 1)   # để truy vết số trước
    digit = [''] * (N + 1)    # chữ số ('0' hoặc '9') đã thêm
    
    q = deque()
    start = 9 % N
    q.append(start)
    visited[start] = True
    parent[start] = -1
    digit[start] = '9'
    
    if start == 0:
        return "9"
    
    while q:
        r = q.popleft()
        for d in ['0', '9']:
            new_r = (r * 10 + int(d)) % N
            if not visited[new_r]:
                visited[new_r] = True
                parent[new_r] = r
                digit[new_r] = d
                if new_r == 0:
                    # reconstruct answer
                    ans = []
                    cur = new_r
                    while cur != -1:
                        ans.append(digit[cur])
                        cur = parent[cur]
                    return ''.join(reversed(ans))
                q.append(new_r)
    return None

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    T = int(data[0])
    ns = list(map(int, data[1:]))
    for n in ns:
        print(smallest_multiple(n))

if __name__ == "__main__":
    solve()
