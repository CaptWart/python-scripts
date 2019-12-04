import os
import csv
import sys

server = sys.argv[1]

print(server)

#Username that is used on the server
uname = input("What is your username? ")
command = input("what command do you want to send? ")

# Loops through csv file
with open(server) as f:
  reader = csv.reader(f)
  your_list = list(reader)
  array_length = len(your_list)

# Send your command to server list in .csv file
  for i in range(array_length):
    host = str(your_list[i])
    print(host[2:len(host)-2])
    os.system('ssh ' + ' ' + uname + '@' + host[2:len(host)-2] + ' ' + command)
