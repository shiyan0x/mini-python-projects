from itertools import combinations_with_replacement
n = str(input().upper()).split()
m= n[0]
p = int(n[1])




list = sorted(list(combinations_with_replacement(m,p)))
for i in list:
    print("".join(i)) 
