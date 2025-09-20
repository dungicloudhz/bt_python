# def solve():
#     N = int(input().strip())
#     arr = list(map(int, input().split()))
    
#     step = 1
#     for i in range(N - 1):
#         swapped = False
#         for j in range(N - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if swapped:  # chỉ in nếu có thay đổi
#             print("Buoc {}: {}".format(step, " ".join(map(str, arr))))
#             step += 1
#         else:
#             break
