n = int(input("N = "))
a = []
b = []
for i in range(1,n+1):
    s = input(f"Nhap gia tri thu {i}: ")
    if s.startswith('-'):
        s2 = s.replace('-','')
        if s2.isdigit() or s2.replace('.','').isdigit():
            a.append(s)
        else:
            b.append(s)
    else:
        if s.isdigit() or s.replace('.','').isdigit():
            a.append(s)
        else:
            b.append(s)
s = 0
for i in a:
    s+=float(i)
print(f"Tong cac phan tu cua A = {s}")

b1 = '-'.join(b)
print(f"B = {b1}")



