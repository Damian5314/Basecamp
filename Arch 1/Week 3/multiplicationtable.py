horizontal=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vertical=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("   ", end="")
for x in horizontal:
    print(f"{x:3}", end="")
print()

for x in horizontal:
    print(f"{x:2}", end="")
    for y in vertical: 
        product= x*y
        print(f"{product:3}", end="")
    print()