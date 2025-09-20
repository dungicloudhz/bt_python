```c
BÀI TẬP 1: Dãy gồm n các số nguyên .Viết chương trình: 
a) Đưa dãy ra màn hình. 
b) Tìm số lớn nhất và nhỏ nhất. 
c) Đưa ra số lớn nhất hoặc bé nhất và vị trí của chúng. 
d) Đưa ra các số xuất hiện k lần (vd k=2).
#include <stdio.h>

// a) In dãy ra màn hình
void printArray(int a[], int n) {
    printf("Day vua nhap: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

// b) Tìm số lớn nhất và nhỏ nhất
void findMaxMin(int a[], int n, int *max, int *min) {
    *max = a[0];
    *min = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] > *max) *max = a[i];
        if (a[i] < *min) *min = a[i];
    }
}

// c) In vị trí số lớn nhất và nhỏ nhất
void printPositions(int a[], int n, int max, int min) {
    printf("Vi tri so lon nhat (%d): ", max);
    for (int i = 0; i < n; i++) {
        if (a[i] == max) printf("%d ", i);  // in chỉ số i
    }
    printf("\n");

    printf("Vi tri so nho nhat (%d): ", min);
    for (int i = 0; i < n; i++) {
        if (a[i] == min) printf("%d ", i);
    }
    printf("\n");
}	// d) In các số xuất hiện đúng k lần
void printKTimes(int a[], int n, int k) {
    printf("Cac so xuat hien %d lan: ", k);
    for (int i = 0; i < n; i++) {
        int count = 0;

        // kiểm tra số a[i] đã xét trước đó chưa
        int daDem = 0;
        for (int j = 0; j < i; j++) {
            if (a[j] == a[i]) {
                daDem = 1;
                break;
            }
        }
        if (daDem) continue;

        // đếm số lần xuất hiện
        for (int j = 0; j < n; j++) {
            if (a[j] == a[i]) count++;
        }

        if (count == k) {
            printf("%d ", a[i]);
        }
    }
    printf("\n");
}











int main() {
    int n, k;
    printf("Nhap so phan tu n: ");
    scanf("%d", &n);

    int a[n];
    printf("Nhap cac phan tu:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    // a)
    printArray(a, n);

    // b)
    int max, min;
    findMaxMin(a, n, &max, &min);
    printf("So lon nhat: %d\n", max);
    printf("So nho nhat: %d\n", min);

    // c)
    printPositions(a, n, max, min);

    // d)
    printf("Nhap k: ");
    scanf("%d", &k);
    printKTimes(a, n, k);

    return 0;
}


 
BÀI TẬP 2: Dãy gồm n các số nguyên .Viết chương trình: 
a) Sắp xếp các số theo thứ tự lớn dần hoặc nhỏ dần (thuật toán nổi bọt) 
b) Sắp xếp các số theo thứ tự lớn dần hoặc nhỏ dần (thuật toán chọn) 
c) Sắp xếp các số theo thứ tự lớn dần hoặc nhỏ dần (thuật toán chèn) -> giải tiếp
#include <stdio.h>
// In mảng
void printArray(int a[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}
// a) Sắp xếp nổi bọt (Bubble Sort)
void bubbleSort(int a[], int n, int tangDan) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if ((tangDan && a[j] > a[j+1]) || (!tangDan && a[j] < a[j+1])) {
                int temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
        printf("Buoc %d: ", i+1);
        printArray(a, n);
    }
}
// b) Sắp xếp chọn (Selection Sort)
void selectionSort(int a[], int n, int tangDan) {
    for (int i = 0; i < n-1; i++) {
        int idx = i;
        for (int j = i+1; j < n; j++) {
            if ((tangDan && a[j] < a[idx]) || (!tangDan && a[j] > a[idx])) {
                idx = j;
            }
        }
        int temp = a[i];
        a[i] = a[idx];
        a[idx] = temp;
        printf("Buoc %d: ", i+1);
        printArray(a, n);
    }
}

	// c) Sắp xếp chèn (Insertion Sort)
void insertionSort(int a[], int n, int tangDan) {
    for (int i = 1; i < n; i++) {
        int key = a[i];
        int j = i - 1;

        while (j >= 0 && ((tangDan && a[j] > key) || (!tangDan && a[j] < key))) {
            a[j+1] = a[j];
            j--;
        }
        a[j+1] = key;

        printf("Buoc %d: ", i);
        printArray(a, n);
    }
}
























int main() {
    int n, choice, order;
    printf("Nhap so phan tu n: ");
    scanf("%d", &n);

    int a[n];
    printf("Nhap cac phan tu:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    printf("Chon thuat toan:\n");
    printf("1. Sap xep noi bot\n");
    printf("2. Sap xep chon\n");
    printf("3. Sap xep chen\n");
    scanf("%d", &choice);

    printf("Chon thu tu (1: tang dan, 0: giam dan): ");
    scanf("%d", &order);

    printf("Mang ban dau: ");
    printArray(a, n);

    switch (choice) {
        case 1: 
            bubbleSort(a, n, order);
            break;
        case 2: 
            selectionSort(a, n, order);
            break;
        case 3: 
            insertionSort(a, n, order);
            break;
        default: 
            printf("Lua chon khong hop le!\n");
    }

    printf("Mang sau khi sap xep: ");
    printArray(a, n);

    return 0;
}


 
#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);

    // Xóa ký tự xuống dòng nếu có
    str[strcspn(str, "\n")] = '\0';

    int len = strlen(str);

    // Liệt kê số lần xuất hiện của mỗi ký tự
    printf("Tan suat xuat hien ky tu:\n");
    for (int i = 0; i < len; i++) {
        int count = 0, daDem = 0;

        // kiểm tra đã đếm ký tự này chưa
        for (int j = 0; j < i; j++) {
            if (str[j] == str[i]) {
                daDem = 1;
                break;
            }
        }
        if (daDem) continue;

        // đếm số lần xuất hiện
        for (int j = 0; j < len; j++) {
            if (str[j] == str[i]) count++;
        }

        printf("chu '%c' co %d lan\n", str[i], count);	    }

    // Cắt 3 ký tự cuối
    if (len > 3) {
        str[len-3] = '\0';
        printf("Cat 3 ky tu cuoi: %s\n", str);
    } else {
        printf("Chuoi ngan hon 3 ky tu, khong cat duoc!\n");
    }

    return 0;
}
1.	Đổi số nguyên thành số nhị phân.Dữ liệu đọc từ tệp. 
char *doinhiphan(long n); 
void doctep(long &n);
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Hàm đổi số nguyên sang nhị phân
char* doinhiphan(long n) {
    // mảng tạm chứa các bit
    char temp[65];  // đủ cho số 64-bit
    int i = 0;

    if (n == 0) {
        return strdup("0");
    }

    while (n > 0) {
        temp[i++] = (n % 2) + '0';  // dư 0 hoặc 1 -> thành ký tự
        n /= 2;
    }
    temp[i] = '\0';

    // đảo ngược chuỗi
    char *result = (char*)malloc(i + 1);
    for (int j = 0; j < i; j++) {
        result[j] = temp[i - j - 1];
    }
    result[i] = '\0';

    return result;
}

// Hàm đọc số nguyên từ tệp
void doctep(long *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file!\n");
        exit(1);
    }
    fscanf(f, "%ld", n);
    fclose(f);
}	int main() {
    long n;
    doctep(&n);

    printf("So doc duoc tu file: %ld\n", n);

    char *bin = doinhiphan(n);
    printf("Dang nhi phan: %s\n", bin);

    free(bin);
    return 0;
}
2.	Đổi số lẻ thành số nhị phân.Dữ liệu đọc từ tệp. 
char *doinhiphan(float x, int n); 
void doctep(float &x, int &n);
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Hàm đổi số thực sang nhị phân
char* doinhiphan(float x, int n) {
    long nguyen = (long)x;
    float tp = x - nguyen;

    // --- Phần nguyên ---
    char temp[65];
    int i = 0;
    if (nguyen == 0) {
        temp[i++] = '0';
    }
    while (nguyen > 0) {
        temp[i++] = (nguyen % 2) + '0';
        nguyen /= 2;
    }
    temp[i] = '\0';

    // Đảo ngược chuỗi phần nguyên
    char *phanNguyen = (char*)malloc(i + 1);
    for (int j = 0; j < i; j++) {
        phanNguyen[j] = temp[i - j - 1];
    }
    phanNguyen[i] = '\0';

    // --- Phần thập phân ---
    char *phanThapPhan = (char*)malloc(n + 1);
    for (int k = 0; k < n; k++) {
        tp *= 2;
        int bit = (int)tp;
        phanThapPhan[k] = bit + '0';
        tp -= bit;
    }
    phanThapPhan[n] = '\0';
	    // Ghép kết quả
    char *ketqua = (char*)malloc(strlen(phanNguyen) + n + 2);
    sprintf(ketqua, "%s.%s", phanNguyen, phanThapPhan);

    free(phanNguyen);
    free(phanThapPhan);

    return ketqua;
}

// Hàm đọc dữ liệu từ file
void doctep(float *x, int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file!\n");
        exit(1);
    }
    fscanf(f, "%f %d", x, n);
    fclose(f);
}

int main() {
    float x;
    int n;
    doctep(&x, &n);

    printf("So doc duoc: %f\n", x);
    printf("So chu so thap phan: %d\n", n);

    char *bin = doinhiphan(x, n);
    printf("Dang nhi phan: %s\n", bin);

    free(bin);
    return 0;
}
3. Sắp xếp dãy các số thực a[0], a[1],..., a[n-1] theo thứ tự tăng dần bằng giải thuật chọn Selection
Sort. Dữ liệu đọc ghi trên tệp.
void selectsort(float a[], int n);
void doctep(float a[], int &n);
void ghitep(float a[], int n);
#include <stdio.h>
#include <stdlib.h>

// Hàm sắp xếp chọn (Selection Sort)
void selectsort(float a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[min_idx]) {
                min_idx = j;
            }
        }
        // đổi chỗ
        float temp = a[i];
        a[i] = a[min_idx];
        a[min_idx] = temp;
    }
}

// Hàm đọc dữ liệu từ file input.txt
void doctep(float a[], int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }
    fscanf(f, "%d", n);
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);
    }
    fclose(f);
}

	// Hàm ghi dữ liệu ra file output.txt
void ghitep(float a[], int n) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }
    fprintf(f, "%d\n", n);
    for (int i = 0; i < n; i++) {
        fprintf(f, "%.2f ", a[i]);
    }
    fprintf(f, "\n");
    fclose(f);
}

int main() {
    float a[100];
    int n;

    // Đọc dữ liệu từ file
    doctep(a, &n);

    // Sắp xếp
    selectsort(a, n);

    // Ghi kết quả ra file
    ghitep(a, n);

    printf("Da sap xep va ghi ket qua ra file output.txt\n");

    return 0;
}

4. Sắp xếp dãy các số thực a[0], a[1],..., a[n-1] theo thứ tự giảm dần bằng giải thuật chèn Insertion
Sort. Dữ liệu đọc ghi trên tệp.
void insertionsort(float a[], int n);
void doctep(float a[], int &n);
void ghitep(float a[], int n);
#include <stdio.h>
#include <stdlib.h>

// Hàm sắp xếp chèn (Insertion Sort giảm dần)
void insertionsort(float a[], int n) {
    for (int i = 1; i < n; i++) {
        float key = a[i];
        int j = i - 1;
        // dịch các phần tử nhỏ hơn key sang phải (để sắp giảm dần)
        while (j >= 0 && a[j] < key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }
}

// Hàm đọc dữ liệu từ file input.txt
void doctep(float a[], int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }
    fscanf(f, "%d", n);
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);
    }
    fclose(f);
}
	
// Hàm ghi dữ liệu ra file output.txt
void ghitep(float a[], int n) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }
    fprintf(f, "%d\n", n);
    for (int i = 0; i < n; i++) {
        fprintf(f, "%.2f ", a[i]);
    }
    fprintf(f, "\n");
    fclose(f);
}

int main() {
    float a[100];
    int n;

    doctep(a, &n);          // đọc dữ liệu từ file
    insertionsort(a, n);    // sắp xếp giảm dần
    ghitep(a, n);           // ghi kết quả ra file

    printf("Da sap xep giam dan va ghi ket qua ra file output.txt\n");
    return 0;
}

 
5. Sắp xếp dãy các số thực a[0], a[1],..., a[n-1] theo thứ tự giảm dần bằng giải thuật nổi bọt Bubble
Sort. Dữ liệu đọc ghi trên tệp.
void bubblesort(float a[], int n);
void doctep(float a[], int &n);
void ghitep(float a[], int n);

#include <stdio.h>
#include <stdlib.h>

// Hàm sắp xếp nổi bọt (Bubble Sort giảm dần)
void bubblesort(float a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (a[j] < a[j + 1]) { // đổi chỗ nếu bên trái < bên phải
                float temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
}

// Hàm đọc dữ liệu từ file input.txt
void doctep(float a[], int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }
    fscanf(f, "%d", n);
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);
    }
    fclose(f);
}
	
// Hàm ghi dữ liệu ra file output.txt
void ghitep(float a[], int n) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }
    fprintf(f, "%d\n", n);
    for (int i = 0; i < n; i++) {
        fprintf(f, "%.2f ", a[i]);
    }
    fprintf(f, "\n");
    fclose(f);
}

int main() {
    float a[100];
    int n;

    doctep(a, &n);          // đọc dữ liệu từ file
    bubblesort(a, n);       // sắp xếp giảm dần
    ghitep(a, n);           // ghi kết quả ra file

    printf("Da sap xep giam dan bang Bubble Sort va ghi ket qua ra file output.txt\n");
    return 0;
}

 
6. Tính n! Dữ liệu đọc từ tệp.
long giaithua(int n);
void doctep(int &n);
#include <stdio.h>
#include <stdlib.h>

// Hàm tính giai thừa
long giaithua(int n) {
    long gt = 1;
    for (int i = 1; i <= n; i++) {
        gt *= i;
    }
    return gt;
}

// Hàm đọc số n từ file input.txt
void doctep(int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }
    fscanf(f, "%d", n);
    fclose(f);
}

// Hàm ghi kết quả ra file output.txt
void ghitep(long kq) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }
    fprintf(f, "%ld\n", kq);
    fclose(f);
}
	
int main() {
    int n;
    doctep(&n);            // đọc n từ file
    long kq = giaithua(n); // tính n!
    ghitep(kq);            // ghi kết quả ra file

    printf("Da tinh %d! = %ld va ghi ket qua ra file output.txt\n", n, kq);
    return 0;
}

 
7. Đếm số lần xuất hiện của số x trong dãy số thực a[0], a[1],..., a[n-1]. Dữ liệu đọc trên tệp.
int demso(float a[], int n, float x);
void doctep(float a[], int &n, float &x);

#include <stdio.h>
#include <stdlib.h>

// Hàm đếm số lần xuất hiện của x trong mảng a
int demso(float a[], int n, float x) {
    int dem = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == x) dem++;
    }
    return dem;
}

// Hàm đọc dữ liệu từ file input.txt
void doctep(float a[], int *n, float *x) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fscanf(f, "%d", n);           // đọc số lượng phần tử
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);   // đọc dãy số
    }
    fscanf(f, "%f", x);           // đọc số cần đếm

    fclose(f);
}
	
// Hàm ghi kết quả ra file output.txt
void ghitep(int kq) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }
    fprintf(f, "%d\n", kq);
    fclose(f);
}

int main() {
    float a[100], x;
    int n;

    doctep(a, &n, &x);            // đọc dữ liệu từ file
    int kq = demso(a, n, x);      // đếm số lần xuất hiện
    ghitep(kq);                   // ghi ra file

    printf("So %.2f xuat hien %d lan (ket qua da ghi ra file output.txt)\n", x, kq);
    return 0;
}

 
8. Tính tổng các số dương trong dãy số thực a[0], a[1],..., a[n-1]. Dữ liệu đọc trên tệp.
float tongduong(float a[], int n);
void doctep(float a[], int &n);

#include <stdio.h>
#include <stdlib.h>

// Hàm tính tổng các số dương trong mảng
float tongduong(float a[], int n) {
    float tong = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] > 0) tong += a[i];
    }
    return tong;
}

// Hàm đọc dữ liệu từ file input.txt
void doctep(float a[], int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fscanf(f, "%d", n);           // đọc số lượng phần tử
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);   // đọc dãy số thực
    }

    fclose(f);
}

	// Hàm ghi kết quả ra file output.txt
void ghitep(float kq) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }
    fprintf(f, "%.2f\n", kq);
    fclose(f);
}

int main() {
    float a[100];
    int n;

    doctep(a, &n);             // đọc dữ liệu từ file
    float kq = tongduong(a, n); // tính tổng số dương
    ghitep(kq);                 // ghi kết quả ra file

    printf("Tong cac so duong = %.2f (da ghi vao file output.txt)\n", kq);
    return 0;
}

 
9. Tính tổng các số âm trong dãy số thực a[0], a[1],..., a[n-1]. Dữ liệu đọc trên tệp.
float tongam(float a[], int n);
void doctep(float a[], int &n);
#include <stdio.h>
#include <stdlib.h>

// Hàm tính tổng các số âm trong mảng
float tongam(float a[], int n) {
    float tong = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] < 0) tong += a[i];
    }
    return tong;
}

// Hàm đọc dữ liệu từ file input.txt
void doctep(float a[], int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fscanf(f, "%d", n);           // đọc số lượng phần tử
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);   // đọc dãy số thực
    }

    fclose(f);
}
	
// Hàm ghi kết quả ra file output.txt
void ghitep(float kq) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }
    fprintf(f, "%.2f\n", kq);
    fclose(f);
}

int main() {
    float a[100];
    int n;

    doctep(a, &n);             // đọc dữ liệu từ file
    float kq = tongam(a, n);   // tính tổng số âm
    ghitep(kq);                // ghi kết quả ra file

    printf("Tong cac so am = %.2f (da ghi vao file output.txt)\n", kq);
    return 0;
}

 
10. Tính giá trị lớn nhất trong dãy số thực a[0], a[1],..., a[n-1]. Dữ liệu đọc trên tệp.
float lonnhat(float a[], int n);
void doctep(float a[], int &n);
#include <stdio.h>
#include <stdlib.h>

// Hàm tìm giá trị lớn nhất trong mảng
float lonnhat(float a[], int n) {
    float max = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] > max) max = a[i];
    }
    return max;
}

// Hàm đọc dữ liệu từ file input.txt
void doctep(float a[], int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fscanf(f, "%d", n);            // đọc số lượng phần tử
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);    // đọc dãy số thực
    }

    fclose(f);
}
	
// Hàm ghi kết quả ra file output.txt
void ghitep(float kq) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }
    fprintf(f, "%.2f\n", kq);
    fclose(f);
}

int main() {
    float a[100];
    int n;

    doctep(a, &n);             // đọc dữ liệu từ file
    float kq = lonnhat(a, n);  // tìm giá trị lớn nhất
    ghitep(kq);                // ghi kết quả ra file

    printf("Gia tri lon nhat = %.2f (da ghi vao file output.txt)\n", kq);
    return 0;
}

 
11. Tính giá trị nhỏ nhất trong dãy số thực a[0], a[1],..., a[n-1]. Dữ liệu đọc trên tệp.
float nhonhat(float a[], int n);
void doctep(float a[], int &n);

#include <stdio.h>
#include <stdlib.h>

// Hàm tìm giá trị nhỏ nhất trong mảng
float nhonhat(float a[], int n) {
    float min = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] < min) min = a[i];
    }
    return min;
}

// Hàm đọc dữ liệu từ file input.txt
void doctep(float a[], int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fscanf(f, "%d", n);            // đọc số lượng phần tử
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);    // đọc dãy số thực
    }

    fclose(f);
}
	
// Hàm ghi kết quả ra file output.txt
void ghitep(float kq) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }
    fprintf(f, "%.2f\n", kq);
    fclose(f);
}

int main() {
    float a[100];
    int n;

    doctep(a, &n);              // đọc dữ liệu từ file
    float kq = nhonhat(a, n);   // tìm giá trị nhỏ nhất
    ghitep(kq);                 // ghi kết quả ra file

    printf("Gia tri nho nhat = %.2f (da ghi vao file output.txt)\n", kq);
    return 0;
}

 
12. Đếm tổng số ký tự là chữ hoa trong một xâu s[]. Dữ liệu đọc từ tệp.
int tongchuhoa(char s[]);
void doctep(char s[]);
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Hàm đếm số ký tự chữ hoa
int tongchuhoa(char s[]) {
    int dem = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (isupper(s[i])) dem++; // kiểm tra ký tự hoa
    }
    return dem;
}

// Hàm đọc xâu từ file input.txt
void doctep(char s[]) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fgets(s, 1000, f); // đọc 1 dòng (tối đa 1000 ký tự)
    fclose(f);

    // Xóa ký tự xuống dòng nếu có
    size_t len = strlen(s);
    if (len > 0 && s[len - 1] == '\n') {
        s[len - 1] = '\0';
    }
}
	
// Hàm ghi kết quả ra file output.txt
void ghitep(int kq) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }
    fprintf(f, "%d\n", kq);
    fclose(f);
}

int main() {
    char s[1000];

    doctep(s);                // đọc xâu từ file
    int kq = tongchuhoa(s);   // đếm chữ hoa
    ghitep(kq);               // ghi kết quả ra file

    printf("So chu hoa trong xau = %d (da ghi vao file output.txt)\n", kq);
    return 0;
}

 
13. Đếm tổng số ký tự là chữ thường trong một xâu s[]. Dữ liệu đọc từ tệp
int tongchuthuong(char s[]);
void doctep(char s[]);

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Hàm đếm số ký tự chữ thường
int tongchuthuong(char s[]) {
    int dem = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (islower(s[i])) dem++; // kiểm tra chữ thường
    }
    return dem;
}

// Hàm đọc xâu từ file input.txt
void doctep(char s[]) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fgets(s, 1000, f); // đọc 1 dòng (tối đa 1000 ký tự)
    fclose(f);

    // Xóa ký tự xuống dòng nếu có
    size_t len = strlen(s);
    if (len > 0 && s[len - 1] == '\n') {
        s[len - 1] = '\0';
    }
}
	
// Hàm ghi kết quả ra file output.txt
void ghitep(int kq) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }
    fprintf(f, "%d\n", kq);
    fclose(f);
}

int main() {
    char s[1000];

    doctep(s);                   // đọc xâu từ file
    int kq = tongchuthuong(s);   // đếm chữ thường
    ghitep(kq);                  // ghi kết quả ra file

    printf("So chu thuong trong xau = %d (da ghi vao file output.txt)\n", kq);
    return 0;
}

 
14. Đổi một xâu s[] từ chữ thường thành chữ hoa. Dữ liệu đọc từ tệp
 char *doichuhoa(char s[]);
void doctep(char s[]);
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Hàm đổi xâu thành chữ hoa
char* doichuhoa(char s[]) {
    for (int i = 0; i < strlen(s); i++) {
        s[i] = toupper(s[i]); // chuyển từng ký tự thành chữ hoa
    }
    return s;
}

// Hàm đọc xâu từ file input.txt
void doctep(char s[]) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fgets(s, 1000, f); // đọc tối đa 1000 ký tự
    fclose(f);

    // Xóa ký tự xuống dòng nếu có
    size_t len = strlen(s);
    if (len > 0 && s[len - 1] == '\n') {
        s[len - 1] = '\0';
    }
}

	// Hàm ghi kết quả ra file output.txt
void ghitep(char s[]) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }
    fprintf(f, "%s\n", s);
    fclose(f);
}

int main() {
    char s[1000];

    doctep(s);             // đọc xâu từ file
    doichuhoa(s);          // đổi sang chữ hoa
    ghitep(s);             // ghi kết quả ra file

    printf("Xau sau khi doi sang chu hoa: %s (da ghi vao output.txt)\n", s);
    return 0;
}

 
15. Đổi một xâu s[] từ chữ hoa thành chữ thường. Dữ liệu đọc từ tệp
char *doichuthuong(char s[]);
void doctep(char s[]);
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Hàm đổi xâu thành chữ thường
char* doichuthuong(char s[]) {
    for (int i = 0; i < strlen(s); i++) {
        s[i] = tolower(s[i]); // chuyển từng ký tự thành chữ thường
    }
    return s;
}

// Hàm đọc xâu từ file input.txt
void doctep(char s[]) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fgets(s, 1000, f); // đọc tối đa 1000 ký tự
    fclose(f);

    // Xóa ký tự xuống dòng nếu có
    size_t len = strlen(s);
    if (len > 0 && s[len - 1] == '\n') {
        s[len - 1] = '\0';
    }
}
	
// Hàm ghi kết quả ra file output.txt
void ghitep(char s[]) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }
    fprintf(f, "%s\n", s);
    fclose(f);
}

int main() {
    char s[1000];

    doctep(s);             // đọc xâu từ file
    doichuthuong(s);       // đổi sang chữ thường
    ghitep(s);             // ghi kết quả ra file

    printf("Xau sau khi doi sang chu thuong: %s (da ghi vao output.txt)\n", s);
    return 0;
}

 
16. Kiểm tra dãy số thực a[0], a[1],..., a[n-1] đã được sắp xếp theo thứ tự tăng dần hay không. Dữ
liệu đọc trên tệp.
int kiemtrasapxep(float a[], int n);
void doctep(float a[], int &n);
#include <stdio.h>
#include <stdlib.h>

// Hàm kiểm tra dãy có tăng dần không
int kiemtrasapxep(float a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        if (a[i] > a[i + 1]) {
            return 0; // sai điều kiện tăng dần
        }
    }
    return 1; // thỏa mãn tăng dần
}

// Hàm đọc dữ liệu từ file input.txt
void doctep(float a[], int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fscanf(f, "%d", n); // đọc số phần tử
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);
    }

    fclose(f);
}
	
int main() {
    float a[1000];
    int n;

    doctep(a, &n);

    if (kiemtrasapxep(a, n)) {
        printf("Day da duoc sap xep tang dan.\n");
    } else {
        printf("Day CHUA duoc sap xep tang dan.\n");
    }

    return 0;
}

 
17. Đếm tổng số ký tự là chữ số trong một xâu s[]. Dữ liệu đọc từ tệp
int tongchusố(char s[]);
void doctep(char s[]);

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Hàm đếm số chữ số trong xâu
int tongchuso(char s[]) {
    int count = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (isdigit(s[i])) { // kiểm tra có phải chữ số không
            count++;
        }
    }
    return count;
}

// Hàm đọc xâu từ file input.txt
void doctep(char s[]) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fgets(s, 1000, f); // đọc tối đa 1000 ký tự
    fclose(f);

    // Xóa ký tự xuống dòng nếu có
    size_t len = strlen(s);
    if (len > 0 && s[len - 1] == '\n') {
        s[len - 1] = '\0';
    }
}
	
int main() {
    char s[1000];
    doctep(s);

    int result = tongchuso(s);
    printf("Tong so ky tu la chu so trong xau: %d\n", result);

    return 0;
}

 
 
#include <stdio.h>
#include <math.h>

// Hàm tính e^x với sai số c
float ex(float x, float c) {
    float sum = 1.0;    // e^x bắt đầu từ 1
    float term = 1.0;   // số hạng đầu tiên (x^0 / 0!)
    int n = 1;

    while (fabs(term) > c) {
        term = term * x / n; // tính số hạng tiếp theo
        sum += term;
        n++;
    }

    return sum;
}

int main() {
    float x, c;
    printf("Nhap x: ");
    scanf("%f", &x);
    printf("Nhap c (sai so > 0): ");
    scanf("%f", &c);

    float result = ex(x, c);
    printf("Gia tri e^%.2f ~ %f\n", x, result);

    return 0;
}	

 
19. Đếm số từ trong một xâu ký tự. Thí dụ chuỗi "Trường học " có 2 từ. Dữ liệu đọc từ tệp
int demtu(char s[]);
void doctep(char s[]);
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Hàm đếm số từ trong xâu
int demtu(char s[]) {
    int count = 0;
    int inWord = 0; // 0 = đang ngoài từ, 1 = đang trong từ

    for (int i = 0; i < strlen(s); i++) {
        if (!isspace(s[i])) { // nếu không phải khoảng trắng
            if (inWord == 0) { // bắt đầu một từ mới
                count++;
                inWord = 1;
            }
        } else {
            inWord = 0; // gặp khoảng trắng thì thoát khỏi từ
        }
    }

    return count;
}
	
// Hàm đọc xâu từ file input.txt
void doctep(char s[]) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fgets(s, 1000, f); // đọc tối đa 1000 ký tự
    fclose(f);

    // Xóa ký tự xuống dòng nếu có
    size_t len = strlen(s);
    if (len > 0 && s[len - 1] == '\n') {
        s[len - 1] = '\0';
    }
}

int main() {
    char s[1000];
    doctep(s);

    int result = demtu(s);
    printf("So tu trong xau: %d\n", result);

    return 0;
}

 
20. Đếm số lần xuất hiện của các ký tự ‘a’,’b’,’c’,...trong xâu s[], có phân biệt chữ hoa chữ thường.
Dữ liệu đọc ghi trên tệp.
void demkytu1(char s[], char kt[],int sl[], int &tskt);
void doctep(char s[]);
void ghitep(char kt[],int sl[], int tskt);
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Hàm đếm số lần xuất hiện của các ký tự a-z, A-Z
void demkytu1(char s[], char kt[], int sl[], int *tskt) {
    *tskt = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (isalpha(s[i])) { // chỉ xét ký tự chữ cái
            int found = 0;
            for (int j = 0; j < *tskt; j++) {
                if (kt[j] == s[i]) {
                    sl[j]++;
                    found = 1;
                    break;
                }
            }
            if (!found) {
                kt[*tskt] = s[i];
                sl[*tskt] = 1;
                (*tskt)++;
            }
        }
    }
}
	
// Hàm đọc xâu từ file input.txt
void doctep(char s[]) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }
    fgets(s, 1000, f);
    fclose(f);

    // xóa ký tự xuống dòng nếu có
    size_t len = strlen(s);
    if (len > 0 && s[len - 1] == '\n') {
        s[len - 1] = '\0';
    }
}

// Hàm ghi kết quả ra file output.txt
void ghitep(char kt[], int sl[], int tskt) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }

    for (int i = 0; i < tskt; i++) {
        fprintf(f, "%c: %d\n", kt[i], sl[i]);
    }

    fclose(f);
}



int main() {
    char s[1000];
    char kt[1000];  // mảng lưu ký tự khác nhau
    int sl[1000];   // mảng lưu số lần xuất hiện
    int tskt;       // tổng số ký tự khác nhau

    doctep(s);
    demkytu1(s, kt, sl, &tskt);
    ghitep(kt, sl, tskt);

    printf("Da ghi ket qua vao output.txt\n");
    return 0;
}	

 
21. Đếm số lần xuất hiện của các ký tự ‘a’,’b’,’c’,...trong xâu s[], không phân biệt chữ hoa chữ
thường Dữ liệu đọc ghi trên tệp.
void demkytu2(char s[], char kt[],int sl[], int &tskt);
void doctep(char s[]);
void ghitep(char kt[],int sl[], int tskt);
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Hàm đếm ký tự (không phân biệt hoa/thường)
void demkytu2(char s[], char kt[], int sl[], int *tskt) {
    *tskt = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (isalpha(s[i])) { // chỉ xét chữ cái
            char ch = tolower(s[i]); // đổi về chữ thường
            int found = 0;
            for (int j = 0; j < *tskt; j++) {
                if (kt[j] == ch) {
                    sl[j]++;
                    found = 1;
                    break;
                }
            }
            if (!found) {
                kt[*tskt] = ch;
                sl[*tskt] = 1;
                (*tskt)++;
            }
        }
    }
}

	// Hàm đọc xâu từ file input.txt
void doctep(char s[]) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }
    fgets(s, 1000, f);
    fclose(f);

    // xóa ký tự xuống dòng nếu có
    size_t len = strlen(s);
    if (len > 0 && s[len - 1] == '\n') {
        s[len - 1] = '\0';
    }
}

// Hàm ghi kết quả ra file output.txt
void ghitep(char kt[], int sl[], int tskt) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }

    for (int i = 0; i < tskt; i++) {
        fprintf(f, "%c: %d\n", kt[i], sl[i]);
    }

    fclose(f);
}




int main() {
    char s[1000];
    char kt[1000];  // mảng lưu ký tự khác nhau
    int sl[1000];   // mảng lưu số lần xuất hiện
    int tskt;       // tổng số ký tự khác nhau

    doctep(s);
    demkytu2(s, kt, sl, &tskt);
    ghitep(kt, sl, tskt);

    printf("Da ghi ket qua vao output.txt\n");
    return 0;
}	

 
22. Nhập số liệu cho dãy số thực a[0], a[1],.., a[n-1] từ tệp. Đếm số lần xuất hiện các phần tử trong
dãy.
void doctep(float a[], int &n);
void demso(float a[], int n, float so[], int sl[], int &tongso);
void ghitep(float so[], int sl[], int &tongso);
#include <stdio.h>
#include <stdlib.h>

// Hàm đọc dữ liệu từ file input.txt
void doctep(float a[], int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fscanf(f, "%d", n); // đọc số phần tử
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);
    }

    fclose(f);
}

// Hàm đếm số lần xuất hiện của từng phần tử
void demso(float a[], int n, float so[], int sl[], int *tongso) {
    *tongso = 0;
    for (int i = 0; i < n; i++) {
        int found = 0;
        for (int j = 0; j < *tongso; j++) {
            if (a[i] == so[j]) { // nếu đã tồn tại
                sl[j]++;
                found = 1;
                break;
            }
        }
        if (!found) { // thêm số mới
            so[*tongso] = a[i];
            sl[*tongso] = 1;	            (*tongso)++;
        }
    }
}
// Hàm ghi kết quả ra file output.txt
void ghitep(float so[], int sl[], int tongso) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }

    for (int i = 0; i < tongso; i++) {
        fprintf(f, "%.2f: %d\n", so[i], sl[i]);
    }

    fclose(f);
}

int main() {
    float a[1000], so[1000];
    int n, sl[1000], tongso;

    doctep(a, &n);
    demso(a, n, so, sl, &tongso);
    ghitep(so, sl, tongso);

    printf("Da ghi ket qua vao output.txt\n");
    return 0;
}
23. Kiểm tra xâu s1[] có chứa xâu s2[] hay không. Dữ liệu đọc từ tệp.
int ktxau(char s1[], char s2[]);
void doctep(char s1[], char s2[]);
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Hàm đọc dữ liệu từ file
void doctep(char s1[], char s2[]) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fgets(s1, 1000, f);   // đọc dòng 1
    fgets(s2, 1000, f);   // đọc dòng 2

    // Xóa ký tự xuống dòng nếu có
    s1[strcspn(s1, "\n")] = '\0';
    s2[strcspn(s2, "\n")] = '\0';

    fclose(f);
}

// Hàm kiểm tra xâu s1 có chứa xâu s2 không
int ktxau(char s1[], char s2[]) {
    if (strstr(s1, s2) != NULL) {
        return 1; // có chứa
    }
    return 0; // không chứa
}
	
int main() {
    char s1[1000], s2[1000];
    doctep(s1, s2);

    if (ktxau(s1, s2))
        printf("Xau s1 CO chua xau s2\n");
    else
        printf("Xau s1 KHONG chua xau s2\n");

    return 0;
}

 
24. Trích n ký tự bên trái của một xâu s[] từ vị trí m. Dữ liệu đọc từ tệp.
char *trichtrai(char s[],int n, int m);
void doctep(char s[],int &n, int &m);
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Hàm đọc dữ liệu từ file
void doctep(char s[], int *n, int *m) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fgets(s, 1000, f); // đọc xâu s
    s[strcspn(s, "\n")] = '\0'; // xóa ký tự xuống dòng

    fscanf(f, "%d", m); // đọc vị trí m
    fscanf(f, "%d", n); // đọc số ký tự n

    fclose(f);
}
	
// Hàm trích n ký tự bên trái của chuỗi s từ vị trí m
char *trichtrai(char s[], int n, int m) {
    int len = strlen(s);

    if (m < 0) m = 0;
    if (m >= len) return "";

    if (m + n > len) n = len - m;

    char *res = (char *)malloc((n + 1) * sizeof(char));
    strncpy(res, s + m, n);
    res[n] = '\0';

    return res;
}

int main() {
    char s[1000];
    int n, m;

    doctep(s, &n, &m);

    char *kq = trichtrai(s, n, m);
    printf("Xau sau khi trich: %s\n", kq);

    free(kq);
    return 0;
}

 
26. Nhập số liệu cho dãy số thực a[0], a[1],..., a[n-1] và một giá trị thực x. Giả sử dãy a[] đã được
sắp xếp theo thứ tự tăng dần. Hãy chèn giá trị x vào dãy sao cho dãy a[] vẫn tăng.Dữ liệu đọc
ghi trên tệp.
void chenx(float a[], int &n,float x);
void doctep(float a[], int &n, float &x);
void ghitep(float a[], int n);
#include <stdio.h>
#include <stdlib.h>

// Đọc dữ liệu từ file
void doctep(float a[], int *n, float *x) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong mo duoc file input.txt\n");
        exit(1);
    }

    fscanf(f, "%d", n);  // đọc số phần tử
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);
    }
    fscanf(f, "%f", x); // đọc giá trị x

    fclose(f);
}

// Ghi dữ liệu ra file
void ghitep(float a[], int n) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong mo duoc file output.txt\n");
        exit(1);
    }

    for (int i = 0; i < n; i++) {
        fprintf(f, "%.2f ", a[i]);
    }
    fclose(f);
}	// Hàm chèn x vào mảng tăng dần
void chenx(float a[], int *n, float x) {
    int i = *n - 1;
    while (i >= 0 && a[i] > x) {
        a[i + 1] = a[i];  // dịch sang phải
        i--;
    }
    a[i + 1] = x;
    (*n)++;
}

int main() {
    float a[1000], x;
    int n;

    doctep(a, &n, &x);

    chenx(a, &n, x);

    ghitep(a, n);

    printf("Da chen x vao day va ghi ra file output.txt\n");

    return 0;
}
27. Tính giá trị lớn nhất và các vị trí của nó trong dãy số thực a[0], a[1],.., a[n-1]. Dữ liệu đọc ghi trên
tệp.
float lonnhat(float a[], int n, int vitri[], int &tongvitri);
void doctep(float a[], int &n);
 void ghitep(int vitri[], int tongvitri, float max);
#include <stdio.h>
#include <stdlib.h>

// Đọc dữ liệu từ file
void doctep(float a[], int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong the mo file input.txt\n");
        exit(1);
    }

    fscanf(f, "%d", n);
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);
    }

    fclose(f);
}
// Hàm tìm giá trị lớn nhất và các vị trí của nó
float lonnhat(float a[], int n, int vitri[], int *tongvitri) {
    float max = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] > max) {
            max = a[i];
        }
    }
    *tongvitri = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == max) {
            vitri[*tongvitri] = i;  // lưu chỉ số
            (*tongvitri)++;
        }
    }
    return max;
}	
// Ghi kết quả ra file
void ghitep(int vitri[], int tongvitri, float max) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong the mo file output.txt\n");
        exit(1);
    }

    fprintf(f, "Gia tri lon nhat: %.2f\n", max);
    fprintf(f, "Cac vi tri: ");
    for (int i = 0; i < tongvitri; i++) {
        fprintf(f, "%d ", vitri[i]);
    }
    fclose(f);
}

int main() {
    float a[1000];
    int n;
    int vitri[1000], tongvitri;
    float max;

    doctep(a, &n);

    max = lonnhat(a, n, vitri, &tongvitri);

    ghitep(vitri, tongvitri, max);

    printf("Da ghi ket qua vao file output.txt\n");

    return 0;
}
28. Tính giá trị nhỏ nhất và các vị trí của nó trong dãy số thực a[0], a[1],.., a[n-1]. Dữ liệu đọc ghi
trên tệp.
float nhonhat(float a[], int n, int vitri[], int &tongvitri);
void doctep(float a[], int &n);
 void ghitep(int vitri[], int tongvitri, float min);
#include <stdio.h>
#include <stdlib.h>

// Đọc dữ liệu từ file
void doctep(float a[], int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong the mo file input.txt\n");
        exit(1);
    }

    fscanf(f, "%d", n);
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);
    }

    fclose(f);
}
// Hàm tìm giá trị nhỏ nhất và vị trí của nó
float nhonhat(float a[], int n, int vitri[], int *tongvitri) {
    float min = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] < min) {
            min = a[i];
        }
    }
    *tongvitri = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == min) {
            vitri[*tongvitri] = i;
            (*tongvitri)++;
        }
    }

    return min;
}	
// Ghi kết quả ra file
void ghitep(int vitri[], int tongvitri, float min) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong the mo file output.txt\n");
        exit(1);
    }

    fprintf(f, "Gia tri nho nhat: %.2f\n", min);
    fprintf(f, "Cac vi tri: ");
    for (int i = 0; i < tongvitri; i++) {
        fprintf(f, "%d ", vitri[i]);
    }

    fclose(f);
}

int main() {
    float a[1000];
    int n;
    int vitri[1000], tongvitri;
    float min;

    doctep(a, &n);

    min = nhonhat(a, n, vitri, &tongvitri);

    ghitep(vitri, tongvitri, min);

    printf("Da ghi ket qua vao file output.txt\n");

    return 0;
}
29. Hãy liệt kê các phần tử xuất hiện trong dãy số thực a[0], a[1],.., a[n-1]. đúng một lần. Dữ liệu
đọc ghi trên tệp.
 void solan1(float a[], int n, float a1[], int &m);
void doctep(float a[], int &n);
 void ghitep(float a1[], int m);
#include <stdio.h>
#include <stdlib.h>

// Đọc dữ liệu từ file
void doctep(float a[], int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong the mo file input.txt\n");
        exit(1);
    }

    fscanf(f, "%d", n);
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);
    }

    fclose(f);
}

// Hàm liệt kê các phần tử xuất hiện đúng 1 lần
void solan1(float a[], int n, float a1[], int *m) {
    *m = 0;
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (a[i] == a[j]) count++;
        }
        if (count == 1) {
            a1[*m] = a[i];
            (*m)++;
        }
    }
}
	// Ghi dữ liệu ra file
void ghitep(float a1[], int m) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong the mo file output.txt\n");
        exit(1);
    }

    fprintf(f, "Cac phan tu xuat hien dung 1 lan:\n");
    for (int i = 0; i < m; i++) {
        fprintf(f, "%.2f ", a1[i]);
    }

    fclose(f);
}

int main() {
    float a[1000], a1[1000];
    int n, m;

    doctep(a, &n);

    solan1(a, n, a1, &m);

    ghitep(a1, m);

    printf("Da ghi ket qua vao file output.txt\n");

    return 0;
}

30. Hãy liệt kê các phần tử xuất hiện trong dãy số thực a[0], a[1],.., a[n-1]. đúng hai lần. Dữ liệu
đọc ghi trên tệp.
 void solan2(float a[], int n, float a2[], int &m);
void doctep(float a[], int &n);
 void ghitep(float a2[], int m);
#include <stdio.h>
#include <stdlib.h>

// Đọc dữ liệu từ file
void doctep(float a[], int *n) {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        printf("Khong the mo file input.txt\n");
        exit(1);
    }

    fscanf(f, "%d", n);
    for (int i = 0; i < *n; i++) {
        fscanf(f, "%f", &a[i]);
    }

    fclose(f);
}

// Kiểm tra 1 phần tử đã có trong mảng chưa
int tontai(float arr[], int m, float x) {
    for (int i = 0; i < m; i++) {
        if (arr[i] == x) return 1;
    }
    return 0;
}
	
// Liệt kê các phần tử xuất hiện đúng 2 lần
void solan2(float a[], int n, float a2[], int *m) {
    *m = 0;
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (a[i] == a[j]) count++;
        }
        if (count == 2 && !tontai(a2, *m, a[i])) {
            a2[*m] = a[i];
            (*m)++;
        }
    }
}

// Ghi kết quả ra file
void ghitep(float a2[], int m) {
    FILE *f = fopen("output.txt", "w");
    if (f == NULL) {
        printf("Khong the mo file output.txt\n");
        exit(1);
    }

    fprintf(f, "Cac phan tu xuat hien dung 2 lan:\n");
    for (int i = 0; i < m; i++) {
        fprintf(f, "%.2f ", a2[i]);
    }

    fclose(f);
}


int main() {
    float a[1000], a2[1000];
    int n, m;

    doctep(a, &n);

    solan2(a, n, a2, &m);

    ghitep(a2, m);

    printf("Da ghi ket qua vao file output.txt\n");

    return 0;
}


```