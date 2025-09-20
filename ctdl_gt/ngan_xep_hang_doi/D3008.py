def eval_prefix(exp: str) -> int:
    stack = []
    # duyệt ngược từ phải sang trái
    for ch in reversed(exp):
        if ch.isdigit():
            stack.append(int(ch))
        else:
            a = stack.pop()
            b = stack.pop()
            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(int(a / b))  # chia lấy phần nguyên
    return stack[-1]

# Đọc input
t = int(input().strip())
for _ in range(t):
    exp = input().strip()
    print(eval_prefix(exp))
