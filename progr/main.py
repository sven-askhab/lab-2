print("Kasimov Ashab")
var = int(input("Введите число: "))
sum = 0
while var > 0:
    rest = var % 10
    sum = sum + rest
    var = var//10
print("Сумма цифр равна:", sum)