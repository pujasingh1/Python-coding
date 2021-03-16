#given integer number n, create a dictionary with the function that creates the square of the number.
 #integer is a number assigned to a function.
print('Enter in a number:')
n = int(input())
d = dict()
for i in range(i,n+1):
  d[i] = i*i
print(d)
