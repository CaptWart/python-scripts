import sys

# Declare variables
file = sys.argv[1]
output = sys.argv[2]

# Opens file
with open (file, "r") as myfile:
  data = myfile.readlines()

# Loops through each word and splits (Seperates) every word into it's own line

for i in range(len(data)):
    words = data[i].split()
    for word in words:
# Looks for ".com" in word
      if ".com" in word:
# Strips out special characters
          word.strip(',')
# Appends any word with ".com" to file
          text = sys.stdout
          sys.stdout = open(output, 'a')
          print(word)
          sys.stdout = text
