flag = [112,101,98,105,105,106,94,113,98,112,126,79,120,55,98,101,92,98,117,51,50,45,108,78,42,89,70,45,108,111,59,58,82,111,115,59,73,78,127,131]

print("".join([chr(flag[i] + 3) for i in range(0,10)]))
print("".join([chr(flag[i] - 3) for i in range(10,20)]))
print("".join([chr(flag[i]  + 6) for i in range(20,30)]))
print("".join([chr(flag[i] - 6) for i in range(30,40)]))