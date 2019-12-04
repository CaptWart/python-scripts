import os
import csv
import sys

# Variable declration and asking for input
file = sys.argv[1]
result = ''

# Looks into the .csv file  that was given
with open(file) as f:
  reader = csv.reader(f)
  your_list = list(reader)
  array_length = len(your_list)

# Loops through csv and check if it's pingable then puts results into new file
for i in range(array_length):
  host = str(your_list[i])
  response = os.system("ping -c 1 -q " + host[2:len(host)-2])

# Checks to see which servers were pingable and then adds to variable
  if response == 0:
    result += host[2:len(host)-2] + ' is up! ' + '\n'
  else:
    result += host[2:len(host)-2] + ' is down! ' + '\n'

# Shows results of test
print(result)
