#n! = 1 * 2 * ... * n, де
#n - введене
#користувачем
#число.
number_input = int(input("Please, enter the number: "))
f = 1
while number_input > 1:
    f = f * number_input
    number_input = number_input - 1
print(f)

