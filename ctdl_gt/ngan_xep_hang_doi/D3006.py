from collections import deque

def process(s: str) -> str:
    left = deque()
    right = deque()
    for ch in s:
        if ch == '<':  # sang trái
            if left:
                right.appendleft(left.pop())
        elif ch == '>':  # sang phải
            if right:
                left.append(right.popleft())
        elif ch == '-':  # backspace
            if left:
                left.pop()
        else:  # ký tự thường
            left.append(ch)
    return ''.join(left) + ''.join(right)

# Đọc input
s = input().strip()
print(process(s))
