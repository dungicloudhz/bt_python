# def solve():
#     T = int(input())
#     for _ in range(T):
#         A, B = map(int, input().split())
#         memo = {}
#         def dfs(s, sq):
#             if (s, sq) in memo:
#                 return memo[(s,sq)]
#             if s == 0 and sq == 0:
#                 return ''
#             if s <= 0 or sq <= 0:
#                 return None
#             res = None
#             for d in range(10):
#                 if d > s or d*d > sq:
#                     break
#                 next_res = dfs(s-d, sq - d*d)
#                 if next_res is not None:
#                     candidate = str(d) + next_res
#                     if res is None or int(candidate) < int(res):
#                         res = candidate
#             memo[(s,sq)] = res
#             return res

#         ans = dfs(A, B)
#         if ans is None:
#             print(-1)
#         else:
#             # loại bỏ số bắt đầu bằng 0
#             ans = ans.lstrip('0')
#             print(ans if ans else '0')

# if __name__ == "__main__":
#     solve()
