import sys

def largest_rectangle_area(heights):
    # heights: list of integers
    n = len(heights)
    stack = []  # stack of indices with increasing heights
    max_area = 0
    for i, h in enumerate(heights):
        # while current height is less than height at stack top, pop and calc area
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            # width extends from last item on stack + 1 to i - 1
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            area = height * width
            if area > max_area:
                max_area = area
        stack.append(i)
    return max_area

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    out_lines = []
    for _ in range(T):
        # skip possible blank lines in tokenized input already removed
        N = int(next(it))
        heights = []
        for _ in range(N):
            heights.append(int(next(it)))
        # append sentinel 0 to flush stack
        heights.append(0)
        ans = largest_rectangle_area(heights)
        out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
