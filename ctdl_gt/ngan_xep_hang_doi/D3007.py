def eval_postfix(exp: str) -> int:
    stack = []
    for ch in exp:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
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
    print(eval_postfix(exp))
