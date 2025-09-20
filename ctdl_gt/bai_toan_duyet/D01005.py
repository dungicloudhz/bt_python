import sys
import math

def main():
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        return
    it = iter(tokens)
    T = int(next(it))
    out_lines = []
    for _ in range(T):
        N = int(next(it))
        K = int(next(it))
        comb = [int(next(it)) for _ in range(K)]
        total_before = 0
        for i in range(K):
            start = 1 if i == 0 else comb[i-1] + 1
            for y in range(start, comb[i]):
                m = N - y
                r = K - (i + 1)  # còn phải chọn r phần tử sau y
                if r < 0:
                    continue
                if m >= r:
                    total_before += math.comb(m, r)
                # nếu m < r thì C(m,r)=0, bỏ qua
        rank = total_before + 1
        out_lines.append(str(rank))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
