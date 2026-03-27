f = open("simple.txt","r")
content = f.read()
f.close()

parts = content.split(",")

result = []
for word in parts:
  result.append(word[::-1])

new_content = ",".join(result)

f = open("simple.txt","w")
f.write(new_content)
f.close()