#compute the factorial of a given number, result printed in single line.(4! is 4*3*2*1 = 24)

def factorial(num):
  if num == 0:
    return 1
  return num = factorial(num-1)
  print('Enter an Integer...')
  num = int(input())
  print(factorial(num))
