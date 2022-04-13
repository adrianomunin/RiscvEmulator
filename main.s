.text
.global _start; _start:


addi x1,x0,32
start:
addi x1,x1,-2
sw x1,256(x1)
blt x1,x0,start
