def even_number(n):
  for i in range(2,n+1,2):
    yield i

for num in even_number(10):
  print(num)