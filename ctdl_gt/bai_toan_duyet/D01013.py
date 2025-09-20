from itertools import permutations

def solve():
    c1, c2 = input().split()
    start, end = sorted([c1, c2])
    # Tạo dãy ký tự từ start -> end
    chars = [chr(i) for i in range(ord(start), ord(end) + 1)]
    # Sinh hoán vị
    perms = sorted("".join(p) for p in permutations(chars))
    for p in perms:
        print(p)

if __name__ == "__main__":
    solve()
