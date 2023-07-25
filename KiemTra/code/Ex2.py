import math
n = int(input("N = "))
s = 0
f = 0
for i in range(1,n+1):
    s=s+i
    f=f+i/math.sqrt(s)
print(f"F({n}) = {f:.7f}")
