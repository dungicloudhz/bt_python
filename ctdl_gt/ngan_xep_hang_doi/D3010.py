import sys

def stock_span(prices):
    n = len(prices)
    stack = []  # stack of indices with prices > current
    spans = [0]*n
    for i, p in enumerate(prices):
        # pop indices with price <= current price
        while stack and prices[stack[-1]] <= p:
            stack.pop()
        if not stack:
            spans[i] = i + 1
        else:
            spans[i] = i - stack[-1]
        stack.append(i)
    return spans

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    out_lines = []
    for _ in range(T):
        # skip possible blank tokens already removed by split
        N = int(next(it))
        prices = [int(next(it)) for _ in range(N)]
        spans = stock_span(prices)
        out_lines.append(" ".join(map(str, spans)))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
