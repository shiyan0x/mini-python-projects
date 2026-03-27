with open("input.txt", "r") as file :
  text = file.read()

  character = len(text)
  lines = text.count("\n")+1 if text else 0
  word = len(text.split())

print("line:", lines)
print("character : ", character)
print("words : ", word)