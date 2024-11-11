from pwn import *


elf = context.binary = ELF("scv")
p = process(env={"LD_PRELOAD" : "libc-2.23.so"})

p.interactive()