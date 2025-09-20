from itertools import combinations

def solve():
    T = int(input().strip())
    for _ in range(T):
        line = input().strip()
        if not line:
            line = input().strip()
        S, k = line.split()
        k = int(k)
        nums = set()
        for idxs in combinations(range(len(S)), k):
            num = "".join(S[i] for i in idxs)
            nums.add(int(num))  # lưu dạng số nguyên
        for num in sorted(nums):
            print(num)

if __name__ == "__main__":
    solve()
