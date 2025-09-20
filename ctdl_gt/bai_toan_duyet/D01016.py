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
