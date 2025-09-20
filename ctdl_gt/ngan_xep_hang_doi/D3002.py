def solve():
    T = int(input().strip())
    for _ in range(T):
        s = input().strip()
        stack = [-1]
        max_len = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:  # ch == ')'
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        print(max_len)

solve()