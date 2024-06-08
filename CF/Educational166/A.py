for _ in range(int(input())):
    n = int(input())
    s = input()

    digit = ""
    letter = ""

    for i in s:
        if i.isdigit():
            digit +=i
        else:
            letter = s[len(digit):]

    # print(digit, letter)
    flag = True
    for i in letter:
        if i.isdigit():
            flag = False
            # print("NO")
            break
    
    if flag:
        for i in letter:
            if i.isdigit():
                flag = False
                break
    if flag:
        if digit != ''.join(sorted(digit)) or letter != ''.join(sorted(letter)):
            flag =False
    print("YES" if flag else "NO")
    








