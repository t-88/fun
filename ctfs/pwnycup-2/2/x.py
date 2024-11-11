import random

data = None
with open("flag.enc","rb") as f:
    data = f.read()


print(len(data))
for i in data:
    print(i,end=",")
    