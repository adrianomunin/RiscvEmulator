.text
.global _start; _start:

abc:
addi x4,x2,4
sub x1,x2,x3
xyz:
sb x0, 8(sp)
bge x1,x2,abc
bge x1,x2,xyz
lui x2,2
jal x2,xyz
