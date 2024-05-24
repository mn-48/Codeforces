# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     # x, y = map(int, input().split())

def solve(test_cases):
    for _ in range(test_cases):
        m, x = map(int, input().split())
        happiness = [0] * (x + 1)

        for _ in range(m):
            c, h = map(int, input().split())
            for j in range(x, c - 1, -1):
                happiness[j] = max(happiness[j], happiness[j - c] + h)

        print(happiness[x])

if __name__ == "__main__":
    t = int(input())
    solve(t)
