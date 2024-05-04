def solve(n, p):
    operations = []

    for i in range(n, 1, -1):
        max_idx = p.index(i)

        # Perform swaps to move the maximum unsorted element to the end
        for j in range(max_idx, n - 2, 2):
            operations.append((j + 1, j + 2))
            p[j], p[j + 1] = p[j + 1], p[j]

    return operations

def main():
    n = int(input())
    p = list(map(int, input().split()))

    operations = solve(n, p)

    print(len(operations))
    for op in operations:
        print(op[0], op[1])

if __name__ == "__main__":
    main()
