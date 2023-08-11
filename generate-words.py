with open("words.txt", "r") as f:
  lines = [line.strip() for line in f.readlines()]

newlines = []

# with open("words2.txt", "w") as f:
#   for i in lines:
#     # print(i)
#     for j in lines:
#       newlines.append(i + " " + j + "\n")
#   newlines[-1] = newlines[-1][:-1]
#   print("writing lines...")
#   f.writelines(newlines)

with open("words-copy.txt", "w") as f:
  for i in lines:
    newlines.append(" " + i + "\n")
  newlines[-1] = newlines[-1][:-1]
  f.writelines(newlines)