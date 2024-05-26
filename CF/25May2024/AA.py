def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def can_be_sorted_by_rotations(n, arr):
    for i in range(n):
        rotated = arr[i:] + arr[:i]
        if is_sorted(rotated):
            return True
    return False

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        arr = list(map(int, data[index + 1:index + 1 + n]))
        index += 1 + n
        if can_be_sorted_by_rotations(n, arr):
            results.append("Yes")
        else:
            results.append("No")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
