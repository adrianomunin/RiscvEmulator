.text
.global _start; _start:


test:
addi x1,x0,0
beq x1,x0,abc
addi x1,x0,0
beq x1,x0,abc
addi x1,x0,0
beq x1,x0,abc
abc:
