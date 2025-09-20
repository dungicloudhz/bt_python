def max_valid_sum(p: str) -> int:
    open_count = 0
    pairs = 0
    for ch in p:
        if ch == '(':
            open_count += 1
        else:  # ')'
            if open_count > 0:
                open_count -= 1
                pairs += 1
    return pairs * 2


def solve():
    import sys
    input_data = [line.strip() for line in sys.stdin if line.strip()]
    T = int(input_data[0])
    for i in range(1, T+1):
        print(max_valid_sum(input_data[i]))


if __name__ == "__main__":
    solve()
