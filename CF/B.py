# # O(nd) Time | O(n) Space

# def minNumberOfCoinsForChange(n, denoms):
#     # Write your code here.
#     numberOfCoins = [float('inf')]*(n+1)
#     numberOfCoins[0] = 0
#     for denom in denoms:
#         for amount in range(len(numberOfCoins)):
#             if denom <= amount: 
#                 numberOfCoins[amount] = min(numberOfCoins[amount], 1+numberOfCoins[amount-denom])
#     # return numberOfCoins[n] if numberOfCoins[n] != float('inf') else -1
#     return numberOfCoins

# denoms = [1,3,6,10, 15]

# ans = minNumberOfCoinsForChange(max(denoms), denoms)
# print(ans)


# for_0_to_15 = [0, 1, 2, 1, 2, 3, 1, 2, 3, 2, 1, 2, 2, 2, 3, 1]
# for_gt_15   = [0, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 3]
# # for change 5 and 8

# for _ in range(int(input())):
#     n = int(input())
#     if n<=15:
#         print(for_0_to_15[n])
#     else:
#         print(n//15+for_gt_15[n%15])
    
   
for _ in range(int(input())):
    n = int(input())
    s1 = input()
    s2 = input()
    
    counter = 1
    
    for i in range(1, n):
        if s1[i] == s2[i-1]:
            counter +=1
        elif s1[i] < s2[i-1]:
            counter = 1
        else:
            i = i-1
            break
    print(s1[:i+1]+s2[i:])
    print(counter)
        