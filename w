n = int(input("Enter the number n: "))
exponent = int(input("Enter the exponent: "))

power = 1

for i in range(exponent):
    power = power * n

print("Power =", power)
