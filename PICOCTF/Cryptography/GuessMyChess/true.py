import hashlib

file = open("cheese_list.txt","r").readlines()
for x in file:
  for v in range(256):
    print(x[:-1]+hex(v),hashlib.sha256((x[:-1]+chr(v)).lower().encode("utf-8")).hexdigest())
    print(hex(v)+x[:-1],hashlib.sha256((chr(v)+x[:-1]).lower().encode("utf-8")).hexdigest())
