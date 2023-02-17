a = int(input())
b = int(input())
c = int(input())
min = min(a, b, c)
max = max(a, b, c)
if a == min: 
if b == max:
mid = c 
else: 
mid = b 
elif b == min: 
if a == max: 
mid = c 
else: 
mid = a 
elif c == min: 
if a == max: 
mid = b 
else: 
mid = a 
print(max, mid, min, sep="\n")