import math

def print_division_info(num1, num2):
  div = math.floor(num1/num2)
  rem = num1 % num2
  print (str(num1) + " divided by " + str(num2) + " is " + str(div) + " remainder " + str(rem))

print_division_info(4, 3)  # should print: 4 divided by 3 is 1 remainder 1
print_division_info(42, 12)  # should print: 42 divided by 12 is 3 remainder 6