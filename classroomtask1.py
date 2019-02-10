import os
ls = []

def list(dir):
 for name in os.listdir(dir):
  ls.append(name)
  print(ls[::-1])

list("Desktop")



