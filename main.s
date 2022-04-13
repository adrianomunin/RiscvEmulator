.text
.global _start; _start:

addi x3,zero,2
addi x2,zero,10
xor x3,x2,x1

test:
addi x1,x0,0
beq x1,x0,abc
addi x1,x0,0
beq x1,x0,abc
addi x1,x0,0
beq x1,x0,abc
abc:
