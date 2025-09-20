def selection_sort_steps(arr):
    n = len(arr)
    for i in range(n - 1):
        # Tìm phần tử nhỏ nhất trong đoạn từ i đến n-1
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Hoán vị với phần tử đầu của đoạn
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # In ra bước
        print(f"Buoc {i+1}: {' '.join(map(str, arr))}")

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    selection_sort_steps(A)
