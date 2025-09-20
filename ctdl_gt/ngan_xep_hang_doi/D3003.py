def has_redundant_parentheses(expr: str) -> bool:
    stack = []
    operators = set("+-*/")
    for ch in expr:
        if ch == ')':
            top = stack.pop()
            has_operator = False
            # pop cho đến khi gặp '('
            while top != '(':
                if top in operators:
                    has_operator = True
                if not stack:  # phòng trường hợp lỗi ngoặc
                    break
                top = stack.pop()
            # nếu trong ngoặc không có toán tử => dư thừa
            if not has_operator:
                return True
        else:
            stack.append(ch)
    return False


def solve():
    import sys
    input_data = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    T = int(input_data[0])
    for i in range(1, T+1):
        expr = input_data[i].replace(" ", "")  # bỏ khoảng trắng
        if has_redundant_parentheses(expr):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solve()
