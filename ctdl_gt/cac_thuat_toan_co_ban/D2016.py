# import math

# def min_squares(N):
#     dp = [float('inf')] * (N+1)
#     dp[0] = 0
#     for i in range(1, N+1):
#         j = 1
#         while j*j <= i:
#             dp[i] = min(dp[i], dp[i - j*j] + 1)
#             j += 1
#     return dp[N]

# def solve():
#     T = int(input())
#     for _ in range(T):
#         N = int(input())
#         print(min_squares(N))

# if __name__ == "__main__":
#     solve()
