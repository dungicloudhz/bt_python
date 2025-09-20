def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    
    # 2 số lớn nhất
    max2 = max(A[-1]*A[-2], A[0]*A[1])
    
    # 3 số lớn nhất
    max3 = max(
        A[-1]*A[-2]*A[-3],  # 3 số lớn nhất
        A[0]*A[1]*A[-1]     # 2 số âm nhỏ nhất + số dương lớn nhất
    )
    
    print(max(max2, max3))

if __name__ == "__main__":
    solve()
