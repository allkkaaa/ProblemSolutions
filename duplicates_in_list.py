#1

lst = list(input().split())
unique = set(lst)
for i in unique:
    lst.remove(i)
    
print(*set(lst))


#2

lst = list(input().split())
d = {}
for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    if d[i] > 1:
        print(i, end=' ')