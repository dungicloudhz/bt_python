```python
D01001. XÂU NHỊ PHÂN CHẴN
Một dãy bít nhị phân 0-1 được gọi là xâu nhị phân chẵn nếu số lượng số 1 là số chẵn (tính cả trường hợp không có số 1 nào).
Cho số nguyên dương n (2 < n < 1a6). Hãy liệt kê các xâu nhị phân chẵn theo thứ tự từ điển.
Input
Chỉ có 1 số n (2 < n < 16).
Output
Ghi ra lần lượt các xâu nhị phân chẵn theo thứ tự từ điển, mỗi xâu trên một dòng.
Các số 0-1 trong mỗi xâu cách nhau đúng một khoảng trống.
Input
	Output
4	0 0 0 0
0 0 1 1
0 1 0 1
0 1 1 0
1 0 0 1
1 0 1 0
1 1 0 0
1 1 1 1

def solve():
    n = int(input().strip())
    limit = 1 << n   # 2^n
    
    for x in range(limit):
        binary = format(x, f'0{n}b')  # dạng chuỗi nhị phân, đủ n bit
        if binary.count("1") % 2 == 0:
            print(" ".join(binary))

solve()	

 
D01002. Xâu AB là dãy ký tự chỉ bao gồm hai chữ cái A và B.
Hãy liệt kê các xâu AB độ dài N thỏa mãn cả 2 điều kiện:
•	Có ít nhất 1 ký tự A
•	Có ít nhất 1 ký tự B
Input
Chỉ có 1 dòng ghi số N (2 < N < 15).
Output
Ghi ra lần lượt các xâu AB thỏa mãn điều kiện theo thứ tự từ điển.
D01002	LIỆT KÊ XÂU AB
Input	Output
4	AAAB
AABA
AABB
ABAA
ABAB
ABBA
ABBB
BAAA
BAAB
BABA
BABB
BBAA
BBAB
BBBA
def solve():
    n = int(input().strip())
    limit = 1 << n   # 2^n
    
    for x in range(limit):
        s = []
        for i in range(n-1, -1, -1):  # từ bit cao xuống thấp
            if (x >> i) & 1:
                s.append("B")
            else:
                s.append("A")
        if "A" in s and "B" in s:
            print("".join(s))

solve()
	

 

D01003. Cho một xâu ký tự S không có ký tự lặp lại. Hãy đưa ra tất cả các tập con của xâu ký tự S theo thứ tự từ điển.
Input:
•	Dòng đầu tiên đưa vào số lượng test T.
•	Những dòng kế tiếp đưa vào các bộ test. 
•	Mỗi bộ test là độ dài xâu ký tự sau đó là nội dung của xâu ký tự S.
•	T, S thỏa mãn ràng buộc: 1≤T≤100; 1≤length(S)≤16.
Output:
•	Đưa ra kết quả mỗi test theo từng dòng.
Input	Output
1
3
abc	a ab abc ac b bc c
def solve():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        s = input().strip()
        
        subsets = []
        limit = 1 << n
        for mask in range(1, limit):  # từ 1 → 2^n - 1 (bỏ tập rỗng)
            subset = []
            for i in range(n):
                if (mask >> i) & 1:
                    subset.append(s[i])
            subsets.append("".join(subset))
        
        # sort theo từ điển
        subsets.sort()
        print(" ".join(subsets))

solve()
	

D01004.Số lộc phát là số chỉ có hai chữ số 6 và 8. Ví dụ 6, 8, 6666, 686886, 88888888 là các số lộc phát. Cho số tự nhiên N không quá 12, hãy liệt kê tất cả các số lộc phát độ dài N theo thứ tự từ nhỏ đến lớn .
Input:
•	Dòng đầu tiên đưa vào số lượng test T.
•	Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test là một số tự nhiên N.
•	T, n thỏa mãn ràng buộc: 1≤T≤10; 1≤N≤12.
Output:
•	Với mỗi test cần đưa ra 2 dòng:
o	Dòng đầu ghi ra số lượng số lộc phát tìm được
o	Dòng thứ hai ghi lần lượt các số theo thứ tự từ nhỏ đến lớn.

Input	Output
2
2
3	4
66 68 86 88
8
666 668 686 688 866 868 886 888
def solve():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        result = []
        limit = 1 << n  # 2^n
        for mask in range(limit):
            num = []
            for i in range(n-1, -1, -1):  # bit cao -> thấp
                if (mask >> i) & 1:
                    num.append('8')
                else:
                    num.append('6')
            result.append("".join(num))
        print(len(result))
        print(" ".join(result))
solve()	
D01005. Cho một tổ hợp chập K của N số nguyên dương đầu tiên (2 < K < N < 15).
Hãy xác định xem đó là tổ hợp thứ bao nhiêu nếu liệt kê tất cả các tổ hợp theo thứ tự tăng dần (tính từ 1).
Input
Dòng đầu ghi số T là số bộ test (T < 10)
Mỗi bộ test gồm 2 dòng
•	Dòng đầu ghi 2 số nguyên dương N và K (2 < K < N < 15)
•	Dòng tiếp theo ghi một tổ hợp chập K của các số nguyên dương từ 1 đến N.
 
Output
Với mỗi bộ test, ghi ra trên một dòng số thứ tự của tổ hợp (tính từ 1, theo thứ tự liệt kê tăng dần).
Input	Output
2
6 4
1 3 5 6
6 4
2 3 4 6	9
12
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
            for y in range(start, comb[i]):	                m = N - y
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

D01006. Cho xâu ký tự S có N chữ số thập phân. Hãy liệt kê các số khác nhau có K chữ số lấy từ K vị trí khác nhau trong xâu S theo thứ tự từ nhỏ đến lớn.
Input
Dòng đầu ghi số bộ test T (T < 10).
Dòng thứ 2 ghi xâu S sau đó là một khoảng trống rồi đến số K (1 < K < N < 20).
Output
Với mỗi bộ test, ghi ra lần lượt các số khác nhau tạo được theo thứ tự từ nhỏ đến lớn.
Input	Output
2
1234 2
4444 2	12
13
14
23
24
34
44
from itertools import combinations

def solve():
    T = int(input().strip())
    for _ in range(T):
        line = input().strip()
        if not line:
            line = input().strip()  # bỏ dòng trống nếu có
        s, k = line.split()
        k = int(k)
        
        numbers = set()
        n = len(s)
        
        for comb in combinations(range(n), k):
            num = "".join(s[i] for i in comb)
            numbers.add(int(num))  # lưu dạng số để so sánh dễ
	        
        result = sorted(numbers)
        for num in result:
            print(num)

solve()


 
D01007. Cho dãy số A[] có N phần tử là các số nguyên dương khác nhau từng đôi một và một số K < N.
Hãy liệt kê tất cả các dãy con khác nhau có K phần tử của A[], mỗi dãy đều được sắp xếp theo thứ tự tăng dần.
Các dãy con được liệt kê lần lượt theo thứ tự từ điển.
Input
Dòng đầu ghi số bộ test, mỗi test có 2 dòng:
•	Dòng đầu ghi hai số N và K (2 < K < N <15)
•	Dòng thứ 2 ghi N số của dãy A[], các số đều nguyên dương, nhỏ hơn 100 và khác nhau từng đôi một.
Output
Với mỗi test, liệt kê tất cả các dãy con thỏa mãn, mỗi dãy con trên một dòng. 
Input	Output
1
4 3
3 2 5 4	2 3 4
2 3 5
2 4 5
3 4 5
from itertools import combinations

def solve():
    T = int(input().strip())
    for _ in range(T):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        arr.sort()  # sắp xếp để đảm bảo thứ tự từ điển
        
        for comb in combinations(arr, k):
            print(" ".join(map(str, comb)))

solve()
	

 
D01008. Cho hai số n và k với k < n. Một tổ hợp chập k của n số nguyên dương đầu tiên được gọi là tổ hợp chẵn nếu tổng các giá trị số trong tổ hợp là một số chẵn.
Viết chương trình liệt kê các tổ hợp chẵn có k phần tử của n số nguyên dương đầu tiên theo thứ tự từ điển.
Input
Chỉ có 1 dòng ghi 2 số n và k (1 < k < n < 16).
Output
Ghi ra lần lượt các tổ hợp chẵn tìm được theo thứ tự từ điển, mỗi tổ hợp trên một dòng. Các số cách nhau đúng một khoảng trống.
Input	Output
5 3	1 2 3
1 2 5
1 3 4
1 4 5
2 3 5
3 4 5
from itertools import combinations

def solve():
    n, k = map(int, input().split())
    for comb in combinations(range(1, n+1), k):
        if sum(comb) % 2 == 0:  # tổng chẵn
            print(" ".join(map(str, comb)))

solve()
	

 
D01009. Xâu tam phân độ dài N được định nghĩa là xâu được tạo bởi 3 ký tự số 0, 1, 2.
Viết chương trình liệt kê các xâu tam phân có thứ tự chẵn (theo thứ tự từ điển, thứ tự tính từ 1).
Input
Chỉ có 1 dòng ghi số N (2 < N < 12).
Output
Ghi ra các xâu tam phân chẵn (kèm theo thứ tự của nó). Xem ví dụ để hiểu rõ hơn cách ghi kết quả.
Input	Output
3	2: 001
4: 010
6: 012
8: 021
10: 100
12: 102
14: 111
16: 120
18: 122
20: 201
22: 210
24: 212
26: 221
from itertools import product
def solve():
    n = int(input().strip())
    alphabet = ['0', '1', '2']
    idx = 1
    for p in product(alphabet, repeat=n):
        if idx % 2 == 0:
            print(f"{idx}: {''.join(p)}")	        idx += 1

solve()
D01010. Hãy liệt kê tất cả các xâu ký tự có độ dài không quá N, chỉ tạo bởi các ký tự A, B, C và thỏa mãn các điều kiện sau:
•	Chứa cả ba ký tự A, B, C
•	Số ký tự A không nhiều hơn số ký tự B, số ký tự B không nhiều hơn số ký tự C
Input
Chỉ có một dòng ghi số N, không quá 12.
Output
Ghi ra lần lượt các xâu thỏa mãn theo thứ tự độ dài từ ngắn nhất đến dài nhất.
Nếu có cùng độ dài thì ghi theo thứ tự từ điển.
Mỗi xâu ghi trên một dòng.
Input	Output
4	ABC
ACB
BAC
BCA
CAB
CBA
ABCC
ACBC
ACCB
BACC
BCAC
BCCA
CABC
CACB
CBAC
CBCA
CCAB
CCBA
from itertools import product

def solve():
    N = int(input().strip())
    chars = ['A', 'B', 'C']
    
    for length in range(3, N+1):  # độ dài tối thiểu là 3
        for p in product(chars, repeat=length):
            s = "".join(p)
            if set(s) == {'A', 'B', 'C'}:  # phải đủ A, B, C
                a, b, c = s.count('A'), s.count('B'), s.count('C')
                if a <= b <= c:
                    print(s)

solve()
	

 
D01011. Hãy liệt kê tất cả các tổ hợp chập K của N số nguyên dương đầu tiên theo thứ tự ngược (tức là thứ tự giảm dần).
Input
•	Dòng đầu ghi số bộ test T (T<10)
•	Mỗi bộ test viết trên một dòng 2 số N và K (1 < K < N < 20)
Output
Với mỗi bộ test, ghi lần lượt các tổ hợp theo thứ tự ngược. Mỗi tổ hợp trên một dòng.
Input	Output
1
5 3	3 4 5
2 4 5
2 3 5
2 3 4
1 4 5
1 3 5
1 3 4
1 2 5
1 2 4
1 2 3
from itertools import combinations

def solve():
    T = int(input().strip())
    for _ in range(T):
        N, K = map(int, input().split())
        combs = list(combinations(range(1, N+1), K))
        for c in reversed(combs):
            print(" ".join(map(str, c)))
solve()
	

 
D01012. Cho hai số N và M với 0 < M ≤ N < 10;
Hãy liệt kê các hoán vị của N số nguyên dương đầu tiên mà số M luôn đứng cuối
Các hoán vị thỏa mãn cần liệt kê theo thứ tự từ điển.
Input
Chỉ có một dòng ghi hai số N và M
Output
            Liệt kê lần lượt các hoán vị thỏa mãn. Mỗi hoán vị trên một dòng.
Input	Output
4 2	1 3 4 2
1 4 3 2
3 1 4 2
3 4 1 2
4 1 3 2
4 3 1 2
import sys
from itertools import permutations

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    M = int(data[1])

    remaining = [i for i in range(1, N+1) if i != M]
    # remaining đã là thứ tự tăng -> permutations sẽ ra theo thứ tự từ điển
    for perm in permutations(remaining):
        out = list(perm) + [M]
        print(" ".join(map(str, out)))

if __name__ == "__main__":
    main()

	
. D01013 Cho hai ký tự khác nhau c1 và c2 đều là chữ cái Tiếng Anh in hoa. Với điều kiện khoảng cách giữa hai ký tự này trong bảng chữ cái là không quá 10 vị trí.
Hãy liệt kê tất cả các hoán vị của dãy ký tự ở giữa hai ký tự c1 và c2.
Kết quả cần in ra theo thứ tự từ điển.
Input
Chỉ có một dòng ghi hai ký tự c1 và c2 (c1 có thể đứng trước c2 hoặc ngược lại nhưng không trùng nhau).
Output
Ghi ra lần lượt tất cả các hoán vị của các chữ cái giữa hai ký tự c1 và c2 theo thứ tự từ điển, mỗi ký tự ghi trên một dòng.
Input	Output
E C	CDE
CED
DCE
DEC
ECD
EDC
from itertools import permutations

def solve():
    c1, c2 = input().split()
    start, end = sorted([c1, c2])
    # Tạo dãy ký tự từ start -> end
    chars = [chr(i) for i in range(ord(start), ord(end) + 1)]
    # Sinh hoán vị
    perms = sorted("".join(p) for p in permutations(chars))
    for p in perms:
        print(p)

if __name__ == "__main__":
    solve()
	

 
D01014. Cho hai số nguyên dương n và k (k ≤ n). 
Hãy liệt kê các bộ k số từ n số nguyên dương đầu tiên thoả mãn tính chất: các số từ trái sang phải có thể trùng nhau và có thứ tự không giảm. 
Ví dụ với n = 3 và k = 2 thì các bộ thoả mãn là: {1,1} {1,2} {1,3} {2,2} {2,3} {3,3}
Với n = 3 và k = 3 thì ta có kết quả như trong test ví dụ. 
Input
Chỉ có 1 dòng ghi 2 số n và k (1 < k ≤ n ≤ 12).
Output
Ghi ra màn hình lần lượt các bộ k số theo mô tả đề bài, mỗi kết quả trên một dòng, các số cách nhau một khoảng trống.
Input	Output
3 3	1 1 1
1 1 2
1 1 3
1 2 2
1 2 3
1 3 3
2 2 2
2 2 3
2 3 3
3 3 3
from itertools import combinations_with_replacement

def solve():
    n, k = map(int, input().split())
    for comb in combinations_with_replacement(range(1, n + 1), k):
        print(" ".join(map(str, comb)))
	if __name__ == "__main__":
    solve()

D01015. Cho hai số N, K.
Ta đã biết sẽ có tất cả C(N,K) tổ hợp của K số tự nhiên trong N số tự nhiên đầu tiên, được đánh số thứ tự từ 1 đến C(N,K).
Ký hiệu C(N,K) là số tổ hợp chập K của N.
Hãy liệt kê các tổ hợp của K số tự nhiên trong N số tự nhiên đầu tiên và có thứ tự là số nguyên tố.
Input
Chỉ có 1 dòng ghi hai số N, K (1 < K < N < 20).
Output
Ghi ra các tổ hợp thoả mãn điều kiện bao gồm cả số thứ tự theo mẫu như trong ví dụ dưới đây.
Input	Output
5 3	2: 1 2 4
3: 1 2 5
5: 1 3 5
7: 2 3 4
import math
from itertools import combinations
import sys

def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    r = int(math.isqrt(x))
    for i in range(3, r+1, 2):
        if x % i == 0:
            return False
    return True
	def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N, K = map(int, data[:2])
    idx = 1
    for comb in combinations(range(1, N+1), K):
        if is_prime(idx):
            print(f"{idx}: {' '.join(map(str, comb))}")
        idx += 1

if __name__ == "__main__":
    main()



 
D01016. Có N người xếp hàng với N cái tên phân biệt. Người ta muốn xếp một người duy nhất luôn đứng ở cuối hàng. Hãy liệt kê tất cả các cách xếp hàng thoả mãn theo thứ tự từ điển.
Input
Dòng đầu ghi số N (1 < N < 10) là số người xếp hàng
Dòng 2 ghi N cái tên khác nhau từng đôi một, mỗi cái tên là một dãy ký tự độ dài không quá 30 và không có khoảng trống.
Dòng 3 ghi tên người luôn đứng cuối hàng. Dữ liệu đảm bảo tên của người đứng cuối luôn có trong danh sách ở dòng 2. 
Output
Ghi ra danh sách tất cả các cách xếp hàng theo thứ tự từ điển tăng dần.
Input	Output
4
DONG TAY NAM BAC
NAM	BAC DONG TAY NAM
BAC TAY DONG NAM
DONG BAC TAY NAM
DONG TAY BAC NAM
TAY BAC DONG NAM
TAY DONG BAC NAM
from itertools import permutations

def solve():
    N = int(input().strip())
    names = input().split()
    fixed = input().strip()
    
    others = [x for x in names if x != fixed]
    
    result = []
    for perm in permutations(others):
        line = list(perm) + [fixed]
        result.append(" ".join(line))
    
    result.sort()
    for line in result:
        print(line)
	
if __name__ == "__main__":
    solve()

D01017. Cho xâu ký tự S có N chữ số thập phân. Hãy liệt kê các số khác nhau có K chữ số lấy từ K vị trí khác nhau trong xâu S theo thứ tự từ nhỏ đến lớn.
Input
Dòng đầu ghi số bộ test T (T < 10).
Dòng thứ 2 ghi xâu S sau đó là một khoảng trống rồi đến số K (1 < K < N < 20).
Output
Với mỗi bộ test, ghi ra lần lượt các số khác nhau tạo được theo thứ tự từ nhỏ đến lớn.
Input	Output
2
1234 2
4444 2	12
13
14
23
24
34
44
from itertools import combinations
def solve():
    T = int(input().strip())
    for _ in range(T):
        line = input().strip()
        if not line:
            line = input().strip()
        S, k = line.split()
        k = int(k)
        nums = set()	        for idxs in combinations(range(len(S)), k):
            num = "".join(S[i] for i in idxs)
            nums.add(int(num))  # lưu dạng số nguyên
        for num in sorted(nums):
            print(num)

if __name__ == "__main__":
    solve()

D01018. Khác với những lời đồn về một môn học cực khó với những kiến thức cao siêu, trong môn Cấu trúc dữ liệu và Giải thuật các bạn cũng được biết đến những thuật toán rất đơn giản như quay lui hoặc sinh kế tiếp để liệt kê xâu nhị phân, tổ hợp, hoán vị theo thứ tự từ điển. Hay công thức quy hoạch động để liệt kê dãy số Fibonacci trong phạm vi không quá 92.
Bài toán của các bạn hôm nay là hãy liệt kê các xâu nhị phân có độ dài N và có thứ tự là một số trong dãy Fibonacci.
Input
Chỉ có 1 dòng ghi số N (2 < N < 15).
Output
Ghi ra các xâu nhị phân có thứ tự là các số trong dãy Fibonacci. Xem ví dụ để hiểu rõ hơn cách ghi kết quả.

Input	Output
3	1: 0 0 0
2: 0 0 1
3: 0 1 0
5: 1 0 0
8: 1 1 1
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
        index += 1	if __name__ == "__main__":
    solve()


D01019. Xâu tam phân độ dài N được định nghĩa là xâu được tạo bởi 3 ký tự A, B, C.
Viết chương trình liệt kê các xâu tam phân có thứ tự lẻ (theo thứ tự từ điển, thứ tự tính từ 1).
Input
Chỉ có 1 dòng ghi số N (2 < N < 12).
Output
Ghi ra các xâu tam phân chẵn (kèm theo thứ tự của nó). Xem ví dụ để hiểu rõ hơn cách ghi kết quả.
Input	Output
3	1: AAA
3: AAC
5: ABB
7: ACA
9: ACC
11: BAB
13: BBA
15: BBC
from itertools import product

def solve():
    N = int(input().strip())
    chars = ['A', 'B', 'C']
    index = 1
    for p in product(chars, repeat=N):
        if index % 2 == 1:   # chỉ lấy thứ tự lẻ
            print(f"{index}: {''.join(p)}")
        index += 1

if __name__ == "__main__":
    solve()

	

D01020. Hãy liệt kê các tổ hợp chập K của N số tự nhiên đầu tiên, nhưng chỉ cần liệt kê các tổ hợp cách nhau đúng K vị trí.
Tức là nếu đánh số thứ tự từ 0 thì cần liệt kê các tổ hợp tại vị trí 0, K, 2K, 3K, … theo thứ tự từ điển.
Input
Chỉ có 1 dòng ghi 2 số N và K (2 < N < 30; 2 < K < 15).
Output
Ghi ra các tổ hợp thoả mãn trên từng dòng, mỗi số cách nhau 1 khoảng trống.
Input	Output
6 3	1 2 3
1 2 6
1 3 6
1 5 6
2 3 6
2 5 6
3 5 6
from itertools import combinations

def solve():
    N, K = map(int, input().split())
    nums = range(1, N+1)
    for idx, comb in enumerate(combinations(nums, K)):
        if idx % K == 0:
            print(" ".join(map(str, comb)))

if __name__ == "__main__":
    solve()
	


 
D01021. Cho một xâu ký tự S có N từ chỉ bao gồm các chữ cái viết hoa.
Hãy liệt kê tất cả các từ khác nhau tạo được bằng cách ghép các từ trong xâu S lại với nhau, có thể ghép với bất cứ số lượng từ 1 đến đủ N từ nhưng vẫn giữ nguyên thứ tự trước sau như trong xâu ban đầu.
Input
Dòng đầu ghi số N (1 < N < 16).
Dòng thứ 2 ghi lần lượt N từ, mỗi từ có độ dài lớn hơn 1 nhưng không quá 20, các từ có thể trùng nhau.
Output
Ghi ra các từ khác nhau tạo được theo thứ tự từ điển.
Input	Output
4
ABA BBA AAA AAA	AAA
AAAAAA
ABA
ABAAAA
ABAAAAAAA
…

def solve():
    import sys
    data = [line.strip() for line in sys.stdin if line.strip()]  # bỏ dòng trống
    
    t = int(data[0])
    results = []
    idx = 1
    for _ in range(t):
        n = int(data[idx]); idx += 1
        arr = list(map(int, data[idx].split())); idx += 1
        arr.sort()
        results.append(" ".join(map(str, arr)))
    print("\n".join(results))
	if __name__ == "__main__":
    solve()
D02002. Cho dãy số A[] gồm có N phần tử đã được sắp xếp tăng dần và số K.
Nhiệm vụ của bạn là kiểm tra xem số K có xuất hiện trong dãy số hay không. Nếu có hãy in ra vị trí trong dãy A[], nếu không in ra “NO”.
Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
Mỗi test bắt đầu bằng số nguyên N và K (N ≤ 100 000, 0 ≤ K ≤ 106).
Dòng tiếp theo gồm N số nguyên A[i] (0 ≤ A[i] ≤ 106), các phần tử là riêng biệt.
Output:
Với mỗi test in ra trên một dòng đáp án tìm được.
Input:	Output
2
5 3
1 2 3 4 5
6 5
0 1 2 3 9 10	3
NO
import sys
import bisect

def solve():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        N, K = int(input_data[idx]), int(input_data[idx+1])
        idx += 2
        A = list(map(int, input_data[idx:idx+N]))
        idx += N
        
        pos = bisect.bisect_left(A, K)
        if pos < N and A[pos] == K:
            results.append(str(pos+1))   # in ra vị trí 1-based
        else:
            results.append("NO")	    print("\n".join(results))

if __name__ == "__main__":
    solve()


D02003. Cho số nguyên dương N và K. Hãy tính NK modulo 109+7.
Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
Mỗi test gồm 1 số nguyên N và K (1 ≤ N ≤ 1000, 1 ≤ K ≤ 109).
Output:
Với mỗi test, in ra đáp án trên một dòng.
Input:	Output
2
2 3
4 2	8
16
MOD = 10**9 + 7

def mod_pow(n, k, mod):
    res = 1
    n %= mod
    while k > 0:
        if k & 1:
            res = (res * n) % mod
        n = (n * n) % mod
        k >>= 1
    return res

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    T = int(input_data[0])
    idx = 1
    results = []
    for _ in range(T):
        N, K = int(input_data[idx]), int(input_data[idx+1])
        idx += 2
        results.append(str(mod_pow(N, K, MOD)))
    print("\n".join(results))

if __name__ == "__main__":
    solve()

	
D02004. Một dãy xâu ký tự G chỉ bao gồm các chữ cái A và B được tạo bởi quy tắc:    
G(1) = A;
G(2) = B;
G(n) = G(n-2)+G(n-1).
Với phép cộng (+) là phép nối hai xâu với nhau.  B
Bài toán đặt ra là tìm ký tự ở vị trí thứ i (tính từ 1) của xâu G(n).
Dữ liệu vào: Dòng 1 ghi số bộ test. Mỗi bộ test ghi trên một dòng 2 số nguyên N và i (1<N<93).
Số i đảm bảo trong phạm vi của xâu G(N) và không quá 18 chữ số.
Kết quả: Ghi ra màn hình kết quả tương ứng với từng bộ test.
Input	Output
2
6 4
8 19	A
B
 
from itertools import combinations

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    N, K = map(int, input_data[:2])
    A = input_data[2:]
    
    results = set()
    for comb in combinations(range(N), K):
        s = "".join(A[i] for i in comb)
        results.add(s)
    
    for val in sorted(results):
        print(val)

if __name__ == "__main__":
    solve()

	

 
D02005. Tại ngân hàng có các mệnh giá bằng 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000. 
Tổng số tiền cần đổi có giá trị bằng N.  
Hãy xác định xem có ít nhất bao nhiêu tờ tiền sau khi đổi tiền?
Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 50).  Mỗi test gồm 1 số nguyên N ( 1 ≤ N ≤ 100 000).
Output: Với mỗi test, in ra đáp án trên một dòng.
Input:	Output
2
70
121
 	2
3
import sys

def solve():
    data = [x for x in sys.stdin.read().strip().split() if x]
    if not data:
        return
    t = int(data[0])
    vals = list(map(int, data[1:1+t]))
    denoms = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    out = []
    for N in vals:
        cnt = 0
        remaining = N
        for d in denoms:
            if remaining == 0:
                break
            use = remaining // d
            if use:
                cnt += use
                remaining -= use * d
        out.append(str(cnt))
    print("\n".join(out))

if __name__ == "__main__":
    solve()
	

D02006. Bạn được giao cho N công việc, công việc thứ i có thời gian bắt đầu là A[i] và kết thúc tại B[i]. Tại một thời điểm, bạn chỉ có thể làm một công việc.
Bạn hãy lựa chọn các công việc một cách tối ưu sao cho số công việc làm được là nhiều nhất.
Input: Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
Mỗi test gồm 1 số nguyên N ( 1 ≤ N ≤ 100 000).
N dòng tiếp theo, mỗi dòng gồm 2 số A[i] và B[i] (0 ≤ A[i] < B[i] ≤ 106).
Output: Với mỗi test, in ra đáp án trên một dòng.
Input	Output
1
6
5 9
1 2
3 4
0 6
5 7
8 9
 	4
import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    res = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        jobs = []
        for _ in range(n):
            a = int(data[idx]); b = int(data[idx+1])
            jobs.append((a, b))	            idx += 2
        # Sắp xếp theo thời gian kết thúc
        jobs.sort(key=lambda x: x[1])
        count = 0
        last_end = -1
        for a, b in jobs:
            if a >= last_end:
                count += 1
                last_end = b
        res.append(str(count))
    print("\n".join(res))

if __name__ == "__main__":
    solve()
D02008. Cho hai số nguyên dương N và S. Hãy lựa chọn các chữ số phù hợp để tạo ra số nhỏ nhất và số lớn nhất có N chữ số sao cho tổng chữ số đúng bằng S.
Input
Chỉ có một dòng ghi hai số N và S. (0 < N <= 100; 0 <= S <= 900)
Output
Ghi ra hai số nhỏ nhất và lớn nhất tìm được, cách nhau một khoảng trống.
Nếu không thể tìm được thì ghi ra “-1 -1”
Input	Output
3 20	299 992
def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    S = int(data[1])

    # Trường hợp vô nghiệm nhanh
    if S == 0:
        if N == 1:
            print("0 0")
        else:
            print("-1 -1")
        return
    if S > 9 * N:
        print("-1 -1")
        return

    # Tạo số lớn nhất (greedy từ trái sang phải)
    s_left = S
    max_digits = []
    for i in range(N):
        take = min(9, s_left)
        max_digits.append(str(take))
        s_left -= take
    max_num = "".join(max_digits)
	    # Tạo số nhỏ nhất
    s_left = S
    min_digits = [0] * N
    # đi từ phải sang trái, mỗi vị trí đảm bảo phần còn lại có thể chứa tối đa 9*(pos)
    for pos in range(N-1, -1, -1):
        # minimal digit we must put here to đảm bảo còn lại không vượt quá 9*pos
        need = max(0, s_left - 9 * pos)
        # need không vượt quá 9 do điều kiện tổng <= 9N
        min_digits[pos] = need
        s_left -= need

    # sau khi phân bố theo cách trên, s_left = 0 và min_digits là giải
    # đảm bảo chữ số đầu khác 0 vì S > 0
    min_num = "".join(str(d) for d in min_digits)

    print(min_num, max_num)

if __name__ == "__main__":
    solve()



 
D02009. Cho dãy số A gồm N phần tử là các số nguyên. Hãy tính tích lớn nhất của 2 hoặc 3 phần tử trong dãy.
Input
Dòng đầu tiên ghi số N (3 ≤ N ≤ 10000)
Dòng thứ 2 ghi N số của dãy A (|Ai| ≤ 1000)
Outpput
Ghi ra kết quả trên một dòng
Input	Output
6
5 10 -2 3 5 2	250
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

	

 
D02010. Khu vui chơi trẻ em thiết kế một cầu thang có N bậc để di chuyển lên đỉnh tháp. Sinh viên PTIT cũng được phép leo lên cầu thang này nhưng nhìn chung chân sinh viên PTIT khá là dài nên có thể đi từ 1 đến K bậc mỗi bước (chứ không chỉ là 1 bậc như trẻ em).
Hãy tính xem sinh viên PTIT có bao nhiêu cách để leo lên đến đỉnh.
Input:
•	Dòng đầu tiên là số lượng bộ test T (T ≤ 100).
•	Mỗi test gồm hai số nguyên dương N và K (1 ≤ N ≤ 100000, 1 ≤ K ≤ 100).
Output:
•	Với mỗi test, in ra đáp án tìm được trên một dòng theo modulo 109+7.
•	MOD = 10**9 + 7
•	
•	def solve():
•	    import sys
•	    input = sys.stdin.read
•	    data = input().split()
•	    
•	    t = int(data[0])
•	    tests = []
•	    max_n = 0
•	    idx = 1
•	    for _ in range(t):
•	        N = int(data[idx])
•	        K = int(data[idx+1])
•	        tests.append((N, K))
•	        max_n = max(max_n, N)
•	        idx += 2
•	    
•	    # Xử lý từng test
•	    for N, K in tests:
•	        dp = [0] * (N + 1)
•	        dp[0] = 1
•	        window_sum = 1  # dp[0]•		•	        for i in range(1, N + 1):
•	            dp[i] = window_sum % MOD
•	            window_sum = (window_sum + dp[i]) % MOD
•	            if i >= K:
•	                window_sum = (window_sum - dp[i - K] + MOD) % MOD
•	        print(dp[N])
•	
•	if __name__ == "__main__":
•	    solve()

 
D03001. Cho một xâu chỉ gồm các kí tự ‘(‘, ‘)’, ‘[‘, ‘]’, ‘{‘, ‘}’. Một dãy ngoặc đúng được định nghĩa như sau:
-     Xâu rỗng là 1 dãy ngoặc đúng.
-     Nếu A là 1 dãy ngoặc đúng thì (A), [A], {A} là 1 dãy ngoặc đúng.
-     Nếu A và B là 2 dãy ngoặc đúng thì AB là 1 dãy ngoặc đúng.
Cho một xâu S. Nhiệm vụ của bạn là xác định xâu S có là dãy ngoặc đúng hay không?
Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
Mỗi test gồm 1 xâu S có độ dài không vượt quá 100 000.
Output:
Với mỗi test, in ra “YES” nếu như S là dãy ngoặc đúng, in ra “NO” trong trường hợp ngược lại.
Input:	Output
2
[()]{}{[()()]()}
[(])	YES
NO
def solve():
    T = int(input().strip())
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for _ in range(T):
        s = input().strip()
        stack = []
        ok = True
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif ch in ")]}":
                if not stack or stack[-1] != pairs[ch]:
                    ok = False
                    break
                stack.pop()
        if stack:
            ok = False
        print("YES" if ok else "NO")

solve()	
D3002. Cho một xâu chỉ gồm các kí tự ‘(‘ và ‘)’. Một dãy ngoặc đúng được định nghĩa như sau:
-     Xâu rỗng là 1 dãy ngoặc đúng.
-     Nếu A là 1 dãy ngoặc đúng thì (A) là 1 dãy ngoặc đúng.
-     Nếu A và B là 2 dãy ngoặc đúng thì AB là 1 dãy ngoặc đúng.
Cho một xâu S. Nhiệm vụ của bạn là hãy tìm dãy ngoặc đúng dài nhất xuất hiện trong xâu đã cho.
Input: Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
Mỗi test gồm một xâu S có độ dài không vượt quá 105 kí tự.
Output: Với mỗi test in ra một số nguyên là độ dài dãy ngoặc đúng dài nhất tìm được.
Input:	Output
3
((()
)()())
()(()))))
 	2
4
6
def solve():
    T = int(input().strip())
    for _ in range(T):
        s = input().strip()
        stack = [-1]
        max_len = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:  # ch == ')'
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        print(max_len)

solve()
	

 
D03003. Cho biểu thức số học, hãy cho biết biểu thức số học có dư thừa các cặp ký hiệu ‘(’,’) ‘ hay không?
Input:
•	Dòng đầu tiên đưa vào số lượng bộ test T;
•	Những dòng tiếp theo mỗi dòng đưa vào một bộ test. Mỗi bộ test là một biểu thức.
Output:
•	Đưa ra kết quả mỗi test theo từng dòng.
Ràng buộc:
•	T, exp thỏa mãn ràng buộc: 1≤T≤100; 2≤length(exp)≤20.
Input	Output
3
((a+b))
(a + (b)/c)
(a + b*(c-d))	Yes
Yes
No
def has_redundant_parentheses(expr: str) -> bool:
    stack = []
    operators = set("+-*/")
    for ch in expr:
        if ch == ')':
            top = stack.pop()
            has_operator = False
            # pop cho đến khi gặp '('
            while top != '(':
                if top in operators:
                    has_operator = True
                if not stack:  # phòng trường hợp lỗi ngoặc
                    break
                top = stack.pop()
            # nếu trong ngoặc không có toán tử => dư thừa
            if not has_operator:
                return True
        else:
            stack.append(ch)
    return False	
def solve():
    import sys
    input_data = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    T = int(input_data[0])
    for i in range(1, T+1):
        expr = input_data[i].replace(" ", "")  # bỏ khoảng trắng
        if has_redundant_parentheses(expr):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    solve()


D03004. Cho một xâu chỉ gồm các kí tự ‘(‘, ‘) và có độ dài chẵn. Hãy đếm số lượng dấu ngoặc cần phải đổi chiều ít nhất, sao cho xâu mới thu được là một dãy ngoặc đúng.
Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
Mỗi test gồm 1 xâu S có độ dài không vượt quá 100 000, chỉ gồm dấu ( và ).
Output:
Với mỗi test, in ra đáp án tìm được trên một dòng.
Input:	Output
4
))((
((((
(((())
)(())(((	2
2
1
3
def min_reversals(s: str) -> int:
    open_count = close_count = 0
    for ch in s:
        if ch == '(':
            open_count += 1
        else:  # ch == ')'
            if open_count > 0:
                open_count -= 1  # ghép được với 1 '('
            else:
                close_count += 1  # không ghép được, thừa ')'
    # Tính số đổi chiều
    return (open_count + 1) // 2 + (close_count + 1) // 2

def solve():
    import sys
    input_data = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    T = int(input_data[0])
    for i in range(1, T+1):
        print(min_reversals(input_data[i]))
	if __name__ == "__main__":
    solve()
D03005. Cho biểu thức P chỉ bao gồm các ký tự mở ngoặc ‘(’ hoặc đóng ngoặc ‘)’. Biểu thức P có thể viết đúng hoặc không đúng. Nhiệm vụ của bạn là tìm tổng độ dài lớn nhất của các biểu thức con viết đúng trong P (các biểu thức đúng không nhất thiết phải liên tiếp nhau).
Chú ý: Độ dài của biểu thức đúng ngắn nhất là 2.
Input:
•	Dòng đầu tiên đưa vào số lượng bộ test T (không quá 100)
•	Những dòng tiếp theo mỗi dòng đưa vào một bộ test. Mỗi bộ test là một biểu thức P được viết trên một dòng (độ dài của P không quá 100).
Output:
•	Đưa ra kết quả mỗi test theo từng dòng.
Input	Output
4
(()(
()()((
((()()())))
()(())(	2
4
10
6
def max_valid_sum(p: str) -> int:
    open_count = 0
    pairs = 0
    for ch in p:
        if ch == '(':
            open_count += 1
        else:  # ')'
            if open_count > 0:
                open_count -= 1
                pairs += 1
    return pairs * 2

def solve():
    import sys
    input_data = [line.strip() for line in sys.stdin if line.strip()]
    T = int(input_data[0])
    for i in range(1, T+1):
        print(max_valid_sum(input_data[i]))

if __name__ == "__main__":
    solve()	
D03007. Hãy viết chương trình chuyển tính toán giá trị của biểu thức hậu tố.
Input:
•	Dòng đầu tiên đưa vào số lượng bộ test T;
•	Những dòng tiếp theo mỗi dòng đưa vào một bộ test. Mỗi bộ test là một biểu thức hậu tố exp. Các số xuất hiện trong biểu thức là các số đơn có 1 chữ số.
Output:
•	Đưa ra kết quả mỗi test theo từng dòng, chỉ lấy giá trị phần nguyên.
Ràng buộc:
•	T, exp thỏa mãn ràng buộc: 1≤T≤100; 2≤length(exp)≤20.
Input	Output
2
231*+9–
875*+9-	-4
34
def eval_postfix(exp: str) -> int:
    stack = []
    for ch in exp:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(int(a / b))  # chia lấy phần nguyên
    return stack[-1]

# Đọc input
t = int(input().strip())
for _ in range(t):
    exp = input().strip()
    print(eval_postfix(exp))
	
D03008. Hãy viết chương trình tính toán giá trị của biểu thức tiền tố.
Input:
•	Dòng đầu tiên đưa vào số lượng bộ test T;
•	Những dòng tiếp theo mỗi dòng đưa vào một bộ test. Mỗi bộ test là một biểu thức tiền tố exp. Các số xuất hiện trong biểu thức là các số đơn có 1 chữ số.
Output:
•	Đưa ra kết quả mỗi test theo từng dòng, chỉ lấy giá trị phần nguyên.
Ràng buộc:
•	T, exp thỏa mãn ràng buộc: 1≤T≤100; 2≤length(exp)≤20.
Input	Output
2
-+8/632
-+7*45+20	8
25
def eval_prefix(exp: str) -> int:
    stack = []
    # duyệt ngược từ phải sang trái
    for ch in reversed(exp):
        if ch.isdigit():
            stack.append(int(ch))
        else:
            a = stack.pop()
            b = stack.pop()
            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(int(a / b))  # chia lấy phần nguyên
    return stack[-1]

# Đọc input
t = int(input().strip())
for _ in range(t):
    exp = input().strip()
    print(eval_prefix(exp))	
D03009. Cho N cột, mỗi cột có chiều cao bằng H[i]. Bạn hãy tìm hình chữ nhật lớn nhất bị che phủ bởi các cột?
Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
Mỗi test bắt đầu bởi số nguyên N (N ≤ 100 000).
Dòng tiếp theo gồm N số nguyên H[i] (1 ≤ H[i] ≤ 109).
Output:
Với mỗi test, in ra diện tích hình chữ nhật lớn nhất tìm được.
Input	Output
2
7
6 2 5 4 5 1 6
3
2 2 2
 	12
6
import sys

def largest_rectangle_area(heights):
    # heights: list of integers
    n = len(heights)
    stack = []  # stack of indices with increasing heights
    max_area = 0
    for i, h in enumerate(heights):
        # while current height is less than height at stack top, pop and calc area
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            # width extends from last item on stack + 1 to i - 1
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            area = height * width
            if area > max_area:

	                max_area = area
        stack.append(i)
    return max_area
def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    out_lines = []
    for _ in range(T):
        # skip possible blank lines in tokenized input already removed
        N = int(next(it))
        heights = []
        for _ in range(N):
            heights.append(int(next(it)))
        # append sentinel 0 to flush stack
        heights.append(0)
        ans = largest_rectangle_area(heights)
        out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()


D03010. Bạn là một nhà đầu tư chứng khoán nổi tiếng. Nhiệm vụ hàng ngày của bạn là tính nhịp tăng giảm của phiên chứng khoán trong N ngày để có thể bắt kịp thị trường. Nhịp chứng khoán của ngày thứ i được định nghĩa là số ngày liên tiếp từ ngày thứ i trở về mà giá chứng khoán bé hơn hoặc bằng với giá chứng khoán của ngày i.
Input: Dòng đầu ghi số bộ test (không quá 10). Mỗi test có 2 dòng.
•	Dòng đầu tiên gồm 1 số nguyên N (1 ≤ N ≤ 105) là số ngày.
•	Dòng tiếp theo gồm N số nguyên A1, A2, …, AN (1 ≤ Ai ≤ 106) là giá chứng khoán của các ngày.
Output
•	In ra N số B1, B2, …, BN trong đó Bi là nhịp chứng khoán của ngày thứ i.
Input	Output
1
7
100 80 60 70 60 75 85	1 1 1 2 1 4 6
 
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
D03011. Cho số tự nhiên n. Hãy in ra tất cả các số nhị phân từ 1 đến n.
Input:
•	Dòng đầu tiên ghi lại số lượng test T (T≤100).
•	Mỗi test là một số tự nhiên n được ghi trên một dòng (n≤10000).
Output:
•	Đưa ra kết quả mỗi test trên một dòng.
Input	Output
2
2
5	1 10
1 10 11 100 101
import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    nums = list(map(int, data[1:]))
    out = []
    for n in nums:
        binaries = [bin(i)[2:] for i in range(1, n+1)]
        out.append(" ".join(binaries))
    print("\n".join(out))

if __name__ == "__main__":
    solve()

	

 
D03012. Cho số tự nhiên N. Hãy tìm số nguyên dương X nhỏ nhất được tạo bởi số 9 và số 0 chia hết cho N. Ví dụ với N = 5 ta sẽ tìm ra  X = 90.
Input:
•	Dòng đầu tiên ghi lại số lượng test T (T≤100).
•	Những dòng kế tiếp mỗi dòng ghi lại một test. Mỗi test là một số tự nhiên N được ghi trên một dòng (N≤100).
Output:
•	Đưa ra theo từng dòng số X nhỏ nhất chia hết cho N tìm được .
Input	Output
2
5
7	90
9009
from collections import deque

def smallest_multiple(N):
    # BFS theo dư mod N
    visited = [False] * (N + 1)
    parent = [-1] * (N + 1)   # để truy vết số trước
    digit = [''] * (N + 1)    # chữ số ('0' hoặc '9') đã thêm
    
    q = deque()
    start = 9 % N
    q.append(start)
    visited[start] = True
    parent[start] = -1
    digit[start] = '9'
    
    if start == 0:
        return "9"
    
    while q:
        r = q.popleft()
        for d in ['0', '9']:
            new_r = (r * 10 + int(d)) % N
            if not visited[new_r]:
                visited[new_r] = True
                parent[new_r] = r
                digit[new_r] = d
                if new_r == 0:
                    # reconstruct answer
                    ans = []
                    cur = new_r
                    while cur != -1:
                        ans.append(digit[cur])
                        cur = parent[cur]
                    return ''.join(reversed(ans))
                q.append(new_r)
    return None

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    T = int(data[0])
    ns = list(map(int, data[1:]))
    for n in ns:
        print(smallest_multiple(n))

if __name__ == "__main__":
    solve()

	

```