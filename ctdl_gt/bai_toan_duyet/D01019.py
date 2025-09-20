from itertools import product

def solve():
    N = int(input().strip())
    chars = ['A', 'B', 'C']
    index = 1
    for p in product(chars, repeat=N):
        if index % 2 == 1:   # chỉ lấy thứ tự lẻ
            print(f"{index}: {''.join(p)}")
        index += 1

if __name__ == "__main__":
    solve()
