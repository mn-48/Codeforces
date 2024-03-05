
for _ in range(int(input())):
    s = input()
    n = len(s)
    one = s.count('1')
    zero = s.count('0')
 
    ans = n
    n0 = 0
    n1 = 0
    for i in range(n):
        n0 += int(s[i] == '0')
        n1 += int(s[i] == '1')
        if n0 <= one and n1 <= zero:
            ans = n-i-1
    print(ans)
    
    
    
    
    