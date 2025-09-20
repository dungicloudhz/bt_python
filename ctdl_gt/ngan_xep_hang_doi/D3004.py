def min_reversals(s: str) -> int:
    open_count = close_count = 0
    for ch in s:
        if ch == '(':
            open_count += 1
        else:  # ch == ')'
            if open_count > 0:
                open_count -= 1  # ghép được với 1 '('
            else:
                close_count += 1  # không ghép được, thừa ')'
    # Tính số đổi chiều
    return (open_count + 1) // 2 + (close_count + 1) // 2


def solve():
    import sys
    input_data = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    T = int(input_data[0])
    for i in range(1, T+1):
        print(min_reversals(input_data[i]))


if __name__ == "__main__":
    solve()
