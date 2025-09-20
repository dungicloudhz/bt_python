from itertools import combinations

def solve():
    T = int(input().strip())
    for _ in range(T):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        arr.sort()  # sắp xếp để đảm bảo thứ tự từ điển
        
        for comb in combinations(arr, k):
            print(" ".join(map(str, comb)))

solve()