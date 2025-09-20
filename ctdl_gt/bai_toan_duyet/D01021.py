def solve():
    N = int(input().strip())
    words = input().split()

    results = set()

    # Sinh tất cả các đoạn con liên tiếp
    for i in range(N):
        s = ""
        for j in range(i, N):
            s += words[j]
            results.add(s)

    # In ra theo thứ tự từ điển
    for w in sorted(results):
        print(w)


if __name__ == "__main__":
    solve()
