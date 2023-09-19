celsius= 0
print("°C", "°F")
for i in range(11):
    fahrenheit=(celsius*9/5)+32
    print(f"{celsius} {int(fahrenheit)}")
    celsius += 10
