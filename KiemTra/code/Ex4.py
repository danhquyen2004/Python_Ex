s = input("Nhap S: ")
dem = 0
for i in s:
    if(i == '!'):
        dem+=1
if dem%2 != 0:
    s = s+ '!'
print(f"Chuoi S sau khi xu ly: {s}")