def solve():
    T = int(input().strip())
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for _ in range(T):
        s = input().strip()
        stack = []
        ok = True
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif ch in ")]}":
                if not stack or stack[-1] != pairs[ch]:
                    ok = False
                    break
                stack.pop()
        if stack:
            ok = False
        print("YES" if ok else "NO")

solve()