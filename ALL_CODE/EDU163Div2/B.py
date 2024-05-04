
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    str_list = [str(num) for num in a]
    result = ''.join(str_list)
    sorted_string = ''.join(sorted(result))
    print("YNEOS"[not(result==sorted_string)::2])





   