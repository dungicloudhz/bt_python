from itertools import combinations

def solve():
    T = int(input().strip())
    for _ in range(T):
        line = input().strip()
        if not line:
            line = input().strip()  # bỏ dòng trống nếu có
        s, k = line.split()
        k = int(k)
        
        numbers = set()
        n = len(s)
        
        for comb in combinations(range(n), k):
            num = "".join(s[i] for i in comb)
            numbers.add(int(num))  # lưu dạng số để so sánh dễ
        
        result = sorted(numbers)
        for num in result:
            print(num)


solve()