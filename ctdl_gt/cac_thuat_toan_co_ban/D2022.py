from itertools import combinations

def solve():
    N, K = map(int, input().split())
    words = input().split()
    
    results = set()
    
    # Sinh tất cả các tổ hợp K chỉ số từ 0 đến N-1
    for indices in combinations(range(N), K):
        # Ghép các từ theo chỉ số
        s = ''.join(words[i] for i in indices)
        results.add(s)
    
    # In theo thứ tự từ điển
    for val in sorted(results):
        print(val)

if __name__ == "__main__":
    solve()
