# def solve():
#     import sys
#     data = sys.stdin.read().strip().split()
#     if not data:
#         return
#     N = int(data[0])
#     S = int(data[1])

#     # Trường hợp vô nghiệm nhanh
#     if S == 0:
#         if N == 1:
#             print("0 0")
#         else:
#             print("-1 -1")
#         return
#     if S > 9 * N:
#         print("-1 -1")
#         return

#     # Tạo số lớn nhất (greedy từ trái sang phải)
#     s_left = S
#     max_digits = []
#     for i in range(N):
#         take = min(9, s_left)
#         max_digits.append(str(take))
#         s_left -= take
#     max_num = "".join(max_digits)

#     # Tạo số nhỏ nhất
#     s_left = S
#     min_digits = [0] * N
#     # đi từ phải sang trái, mỗi vị trí đảm bảo phần còn lại có thể chứa tối đa 9*(pos)
#     for pos in range(N-1, -1, -1):
#         # minimal digit we must put here to đảm bảo còn lại không vượt quá 9*pos
#         need = max(0, s_left - 9 * pos)
#         # need không vượt quá 9 do điều kiện tổng <= 9N
#         min_digits[pos] = need
#         s_left -= need

#     # sau khi phân bố theo cách trên, s_left = 0 và min_digits là giải
#     # đảm bảo chữ số đầu khác 0 vì S > 0
#     min_num = "".join(str(d) for d in min_digits)

#     print(min_num, max_num)

# if __name__ == "__main__":
#     solve()
