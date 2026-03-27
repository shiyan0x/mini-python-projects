file = open("input.txt")

for i in file:
  if i.strip:
    num=int(i)
  if (num%2 == 0 ):
    even = open("even.text","a")
    even.write(str(num))
    even.write("\n")

  else:
    odd = open("odd.text","a")
    odd.write(str(num))
    odd.write("\n")
    
               
