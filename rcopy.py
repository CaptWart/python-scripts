import os
import csv
import sys

file = sys.argv[1]
server = sys.argv[2]

print(file)
print(server)

#Username that is used on the server
uname = input("What is your username? ")

# Loops through csv file
with open(server) as f:
  reader = csv.reader(f)
  your_list = list(reader)
  array_length = len(your_list)

# Send SCP command to server list in .csv file
  for i in range(array_length):
    host = str(your_list[i])
    print(host[2:len(host)-2])
    os.system('scp ' + file + ' ' + uname + '@' + host[2:len(host)-2] + ':/home/' + uname)
