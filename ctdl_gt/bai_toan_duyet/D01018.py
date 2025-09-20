def fibonacci_up_to(n):
    fib = [1, 2]
    while fib[-1] + fib[-2] <= n:
        fib.append(fib[-1] + fib[-2])
    return set(fib)

def solve():
    N = int(input().strip())
    total = 2 ** N
    fib_set = fibonacci_up_to(total)
    
    index = 1
    for i in range(total):
        s = format(i, f'0{N}b')   # xâu nhị phân độ dài N
        if index in fib_set:
            print(f"{index}: {' '.join(s)}")
        index += 1

if __name__ == "__main__":
    solve()
