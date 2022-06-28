import math
number_x = float(input("Please, enter your  number: "))
number_y = number_x-math.floor(number_x)
round_y = round(number_y,2)
print(round_y)
print(int((number_x - int(number_x))*10))